#include <math.h>
#include <stdio.h>

void main(){
    int a, b;
    
    printf("enter first number: ");
    scanf("%d", &a);
    printf("enter second number: ");
    scanf("%d", &b);
    
    printf("num1 raised to num2 is: %f", pow(b,a));
}