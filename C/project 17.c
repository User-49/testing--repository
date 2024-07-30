#include <stdio.h>

void main(){
    int sum=0 , pay,n=10;
    while (n)
    {
        printf("enter overtime hours of employee %d: ",11-n);
        scanf("%d",&pay);
        pay *= 12;
        printf("amount to be paid to employee %d : %d\n\n",11-n,pay);
        sum=sum + pay;
        n--;
    }
    printf("total amount to be paid: %d",sum);
    scanf("%d");
}