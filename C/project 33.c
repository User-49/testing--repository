#include <stdio.h>
void main(){
int flag = 0,i,x;
printf("enter number: ");
scanf("%d",&x);
if (!(x%2)) flag = 1;
for  (i = 3; i<=x/2; i +=2) if (i%x) flag = 1;
if (flag) printf("not prime\n");
else printf("prime\n");
}
