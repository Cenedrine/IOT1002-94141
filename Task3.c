/**
 * @file Task3.c
 *@brief Demonstrates simpler functionsfor the assignment
 *
 *This program includes functions like printing a message and add two numbers,
 *with comments for droxy to documment/read
 */
#include<stdio.h>
/**
 * @brief Prints a string message
 * @param[in] Message is the text that will be printed on screen
 */
  
float PrintMessage (char Message[10])
{
    printf ("%s",Message);  ///< Prints the message and adds a newline
}
  
/**
 * @brief Adds two intergers
 * @param[in] num1 is the first number
 * @param[in] num2 is the second number
 * @return int The sum of both num1 and num2
 */
float AddNumbers(int num1, int num2)
{
    int sum = num1 + num2;  ///< this stores the sum of the numbers
    return sum;
}
  
/**
 * @brief Main function
 * @returnint Returns 0 if the program is successfully launched
 */
int main()
{
    printf("This is the main function!"); /// this where the message is printed
}

