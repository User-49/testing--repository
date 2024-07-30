#include <stdio.h>
#include <math.h>

void main(){
    int n = 1, temp, sum;
    while (n!=500)
    {   temp = n;
        sum = 0;
        while (temp)
        {
            sum +=  pow(temp%10,3);
            temp /=10;
        }
        (n==sum?printf("%d\n",n):0) ;
        n++;
    }
    scanf("%d");   
}
