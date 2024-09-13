#include <stdio.h>
#include <math.h>
void main(){
int temp,x ;double y;
printf("enter value of x: ");
scanf("%d",&x);
if (x%2==0) {printf("not prime\n");return;}
y = pow(x,0.5);
printf("%lf",y);
for (temp=3;temp<=y;temp=temp+2)
	if ((x%temp) == 0) {printf("not prime\n");return;}
printf("prime\n")
;}
