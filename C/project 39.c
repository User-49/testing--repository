#include<stdio.h>
void main(){
int x=5,y=5;
func(&x,&y);
printf("%u %u\n",&x,&y);
}
void func(int *,int *);
void func(int *a,int *b){
    printf("[%d %d]\n",*a,*b);
printf("(%u %u)\n",a,b);
printf("(%u %u)\n",&a,&b);
}
