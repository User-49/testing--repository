#include <stdio.h>
int square(int num);
void main(){
int num;
printf("enter the number: ");
scanf("%d",&num);
printf("square of the number: %d\n",square(num));
}
int square(int num){
return (num*num);
}
