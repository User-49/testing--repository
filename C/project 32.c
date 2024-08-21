#include <stdio.h>

int main() {
int f, c;
printf("Enter the temperature in Fahrenheit: ");
scanf("%d", &f);
printf("You entered: %d\n", f);
c = (5.0 / 9.0) * (f - 32);
printf("Temperature in Celsius is: %d\n", c);
scanf("%d");
return 0;
}