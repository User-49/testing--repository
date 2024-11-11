#include <stdio.h>
void main(){
int arr[]={0,1,2,3,4,5,6,7,8,9};
int *a, *b;
a=&arr[0];
b=&arr[10];
printf("a:%u\nb:%u\nb-a:%u\n",a,b,b-a);
}