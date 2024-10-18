#include <stdio.h>
void func1();
void func2();

void func1(){
static int count = 0 ;
count++;
}

void func2(){
static int count=0;
count++;
}
void main(){
printf("%d",count);
func1();
printf("%d",count);
func2();
printf("%d", count);
}
