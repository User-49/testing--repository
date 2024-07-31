#include <stdio.h>
/*using fflush function*/
/*and vernurability in scanf funtion for char values*/

void main(){
    char a,b;
    scanf("%c",&b);
    fflush(stdin);
    scanf("%c",&a);
    printf("b is : %c", b);
    printf("\na is: %c",a);
    scanf("%d");
}