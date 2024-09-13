/*my first menu driven program*/

#include <stdio.h>
int num1,num2,choice,flag;
char temp;
void main(){
    for (;;){
        printf("--------------------------------------------\n");
        printf("what do wish to do: \n");
        printf("1. print factorial\n");
        printf("2. check prime\n");
        printf("3. check even odd\n");
        printf("4. exit\n");
        printf("\nchoice: ");
        scanf("%d",&choice);
        printf("--------------------------------------------\n\n");
        if (choice==4){
            printf("\nyou have exited the program\n");
            printf("**********************************************\n");
            break;
        }
        printf("enter the number: ");
        scanf("%d",&num1);
	switch (choice){
            case 1:
                for (num2 = 1;num1;num1--)
                    num2 *= num1;
                printf("factorial of number is: %d\n",num2);
                break;
            case 2:
                flag = 0;
                for (num2 = 2;num2 <= (num1/2);num2++)
                        if (num1%num2 == 0)
                            flag =1;
                (flag?printf("given number is not a prime\n"):printf("the given number is a prime\n"));
                break;
            case 3:
                (num1%2?printf("the given number is odd\n"):printf("the given number is even\n"));
                break;
            default:
                printf("invalid choice, press enter to go back");
        }
    printf("\nenter anything to go back");
    scanf(" %c",&temp);
    }
}
