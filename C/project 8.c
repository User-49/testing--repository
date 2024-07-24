#include <stdio.h>

/*It doesn't detect that value, it returns it. It reads an integer and puts it inside num. The return value of scanf is not the value it reads from user input but number of values read, which in your case can be a maximum of 1.

*/

void main(){
    printf("enter the number: ");
    int num = scanf("%d", &num);
    printf("%d",num);
}