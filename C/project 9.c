#include <stdio.h>

/*to find sum of 5 digits of a number*/

void main(){
    int num , sum, temp;
    printf("enter a 5 digit number: ");
    scanf("%d", &num);
    sum += num%10;
    num = num/10;
    sum += num%10;
    num = num/10;
    sum += num%10;
    num = num/10;
    sum += num%10;
    num = num/10;
    sum += num%10;
    num = num/10;
    printf("the sum of digits of number: %d", sum);
}