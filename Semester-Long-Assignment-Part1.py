import subprocess
import os
import pandas as pd

CSV_FILE = "/media/sf_VBs/EmployeeNames.csv"

USERNAME_SET = set()
GROUPNAME_SET = set()
new_users = 0
new_groups = 0

if os.geteuid() != 0:
   print ("This script must be run as root. Use sudo.")
   exit (1)

def user_exists(username):
    try:
        subprocess.run(['id', username], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def group_exists(groupname):
    try:
        subprocess.run(['getent','group', groupname], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def create_group(groupname):
    subprocess.run(['groupadd',groupname], check=True)

def create_user(username, groupname):
    subprocess.run(['useradd','-m','-g', groupname, username], check=True)

try:
    df = pd.read_csv(CSV_FILE, engine='python')
except Exception as e:
    print(f"[ERROR] Failed to load CSV file: {e}")
    exit(1)

for index, row in df.iterrows():
    first = str(row.get('FirstName','')).strip()
    last = str(row.get('LastName','')).strip()
    dept = str(row.get('Department','')).strip()

    if not first or not last or not dept:
        print(f"[SKIP] Missing data on row {index + 2}")
        continue

    username = (first[0] + last[:7]).lower()

    if username in USERNAME_SET:
        print (f"[SKIP] Duplicate username in file: {username}")
        continue

    USERNAME_SET.add(username)

    if dept not in GROUPNAME_SET:
        if not group_exists(dept):
            try:
                create_group(dept)
                new_groups += 1
                print (f"[GROUP CREATED] {dept}")
            except subprocess.CalledProcessError:
                print (f"[Error] Failed to create group: {dept}")
                continue
        else:
             print(f"[INFO] Group already exists: {dept}")
        GROUPNAME_SET.add(dept)

    if not user_exists(username):
        try:
            create_user(username, dept)
            new_users += 1
            print (f"[USER CREATED] {username} -> {dept}")
        except subprocess.CalledProcessError:
            print (f"[ERROR] Failed to create user: {username}")
    else:
         print (f"[ERROR] User already exists: {username}")

print ("\n---Summary ---")
print (f"New users added: {new_users}")
print (f"New groups added: {new_groups}")

