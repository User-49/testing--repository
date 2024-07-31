#include <stdio.h>
void main(){
    int a,b;
    float c,d;
    char e,f;
    
    a = 65.0;
    b = 'A';
    c = 65;
    d = 'A';
    e = 65;
    f = 65.0;
    
    /* integer=65, float=65.0, char = 'A'*/
    
    printf("float in integer: %d", a);
    printf("\nchar in integer: %d", b);
    printf("\ninteger in float: %f", c);
    printf("\nchar in float: %f", d);
    printf("\ninteger in char: %c", e);
    printf("\nfloat in char: %c", f);
    scanf("%d");
}