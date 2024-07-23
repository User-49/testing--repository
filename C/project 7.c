#include <stdio.h>
void main(){
    /*float_variable = integer_operand [operator] float_operand*/
    float a;
    a = 6/4.0;
    printf("%f",a);
    
    /*float_variable = integer_operand [operator] integer_operand*/
    float k;
    k = 6/4;
    printf("\n%f",k);
    
    /*integer_variable = integer_operand [operator] integer_operand*/
    int x;
    x = 6/4;
    printf("\n%d", x);
    
    /*integer_variable = integer_operand [operator]float_operand*/
    int s;
    s = 6/4.0;
    printf("\n%d", s);
}