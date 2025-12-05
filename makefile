CC = gcc
CFLAGS = -Wall -g
EXEC = MyProgram
OBJ = SourceFile1.o SourceFile2.o
all: $(EXEC)
$(EXEC): $(OBJ)
	$(CC) $(CFLAGS) -o $(EXEC) $(OBJ)
SourceFile1.o: SourceFile1.c HeaderFile.h
	$(CC) $(CFLAGS) -c SourceFile1.c
SourceFile2.o: SourceFile2.c HeaderFile.h
	$(CC) $(CFLAGS) -c SourceFile2.c
clean:
	rm -f $(OBJ) $(EXEC)

