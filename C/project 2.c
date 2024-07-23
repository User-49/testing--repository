#include <stdio.h>

void main(){
    float sub1,sub2,sub3,sub4,sub5,sum;
    
    printf("enter marks(5 subjects): ");
    scanf("%f %f %f %f %f", &sub1,&sub2,&sub3,&sub4,&sub5);
    
    sum = sub1+sub2+sub3+sub4+sub5;
    
    printf("\npercentage marks: %f", sum*0.2);
    printf("aggregate marks: %f", sum);
}