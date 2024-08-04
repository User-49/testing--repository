#include <stdio.h>
void main(){
    float z;
    char a=65.0, b='B', c='C';
    
    printf("%d", a);
    printf("\n%f", a);
    printf("\n%c", a);
    
    printf("\n\n%c", a+c-b);
    printf("\n%d", a+c-b);
    printf("\n%f", a+c-b);

    printf("\n\n%f", 10);
    printf("\n%d", 10.0);

    printf("\n\n%c", 65.0);
    printf("\n%c", 65);
    scanf("%d");
}