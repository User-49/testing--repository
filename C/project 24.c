#include <stdio.h>
void main(){
    int num,positive,negative,zero;
    positive=negative=zero=0;
    char choice;
    do
    {
        printf("\nEnter a number: ");
        scanf("%d",&num);
        fflush(stdin);
        (num<0?negative++:(num>0?positive++:zero++));
        printf("Do you wish to continue(y/n): ");
        scanf("%c",&choice);
        fflush(stdin);
    }while (choice=='y');

    printf("\npositive numbers: %d\nnegative numbers: %d\nzeros: %d",positive,negative,zero);
    scanf("\n %d enter 'q' to exit");
}