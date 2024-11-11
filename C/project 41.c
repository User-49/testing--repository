#include <stdio.h>
void main(){
    int num,factors[100],j=0;
    printf("enter the number: ");
    scanf("%d",&num);
    for (int i=2;i<=num;i++){
        if (!(num%i)) {factors[j]=i;num/=i;i=2;j++;}
    }
    for (int i=0;i<j;i++) printf("%d, ",factors[i]);
}