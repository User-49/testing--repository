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
        switch (choice){
            case 1:
                printf("enter the number: ");
                scanf("%d", &num1);
                for (num2 = 1;num1;num1--)
                    num2 *= num1;
                printf("factorial of number is: %d\n",num2);
                printf("press enter to back");
                fflush(stdin);
                scanf("%c", temp);
                break;
            case 2: 
                printf("enter the number: ");
                scanf("%d",&num1);
                flag = 0;
                

                
        }
    }
}