#include<stdio.h>
void main(){
int x=5,y=5;
func(&x,&y);
printf("%u %u",&x,&y);
}
void func(int *a,int *b);
void func(int *a,int *b){
printf("(%d %d)",a,b);
printf("(%u %u)",&a,&b);
}
