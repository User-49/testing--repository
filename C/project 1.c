#include <stdio.h>

void main(){
    int principal, year;
    float simple_intrest, roi;

    printf("Enter principal value: ");
    scanf("%d", &principal);
    printf("Enter roi per annum: ");
    scanf("%f", roi);
    printf("Enter number of years: ");
    scanf("%f", &year);

    printf("simple intrestis: %f", principal*roi*year/100);
}