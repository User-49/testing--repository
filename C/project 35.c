

// C Program to illustrate how to use #define to declare 
// constants 
#include <stdio.h> 
  
// Defining macros with constant value 
#define PI 3.14159265359 
  
int main() 
{ 
  
    int radius = 21; 
    int area; 
  
    // Using macros to calculate area of circle 
    area = PI * radius * radius; 
  
    printf("Area of Circle of radius %d: %d\n", radius, area); 
  
    return 0; 
}
