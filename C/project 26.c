#include <math.h>
#include <stdio.h>

void main(){
    /*initializing variables*/
    int num1,num2,num3,choice;
    char exit;
    do
    {
        printf("--------------------------------------\n");
        printf("what do you wish to do..?\n");
        printf("1. print fctorial\n");
        printf("2. check if prime\n");
        printf("3. check odd or even\n");
        printf("4. exit\n\n");
        scanf("%d",&choice);
        fflush(stdin);
        printf("---------------------------------------\n");
        switch (choice){
            case 1:
                printf("enter a number: ");
                scanf("%d",&num1);
                fflush(stdin);
                for (num2=1;num1;num1--)
                    num2*=num1;
                printf("factorial of given number is: %d",num2);
                printf("\npress enter to go back");
                scanf("%c");
                fflush(stdin);
                break;
            case 2:
                printf("enter a number: ");
                scanf("%d",&num1);
                fflush(stdin);
                for (num2=2;num2<(num1/2);num2++)
                    if (num1%num2 == 0){
                        printf("%d is not a prime number\n",num1);
                        goto out;
                    }
                printf("%d is a prime number\n",num1);
                out:
                break;
            case 3:
                printf("enter a number: ");
                scanf("%d",&num1);
                fflush(stdin);
                if (num1%2==0)
                    printf("%d is a even number\n", num1);
                else printf("%d id a an even number\n");
                break;
            case 4:
                printf("\n**************************************");
                printf("\t\t---you have exited the prgram---");
            default: 
                printf("invalid input, press enter to go back");
                scanf("%c");   
            }
    } while (1);
}