#include <stdio.h>
int choice;

void main(){
    for (;;){
        printf("Enter choice: ");
        scanf("%d",&choice);
        fflush(stdin);
        switch (choice){
            case 1:
            printf("you have entered '1'\n");
            break;
            case 2:
            printf("you have entered '2'\n");
            break;
            default:
            printf("you have entered something else\n");

        }
    }
}