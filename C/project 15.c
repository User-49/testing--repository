#include <stdio.h>

void main(){
    char x;

    printf("Enter the character: ");
    scanf("%c",&x);
    if ('A'<=x && x<'Z') printf("entered character is UpperCase");
    else if ('a'<=x && x<'z') printf("entered character is LowerCase");
    else printf("entered character is a special character");

}