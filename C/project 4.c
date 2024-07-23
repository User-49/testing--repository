#include <stdio.h>
void main(){
    float z;
    char a='A', b='B', c='C';
    
    printf("%d", a);
    printf("\n%f", a);
    printf("\n%c", a);
    
    printf("\n\n%c", a+c-b);
    printf("\n%d", a+c-b);
    printf("\n%f", a+c-b);
}