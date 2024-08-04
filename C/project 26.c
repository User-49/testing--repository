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
<<<<<<< HEAD
        printf("1. print factorial\n");
=======
        printf("1. print fctorial\n");
>>>>>>> 16c4f0275291b7acb2408f0fbfb078433fd4017a
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
<<<<<<< HEAD
                printf("\nfactorial of given number is: %d",num2);
=======
                printf("factorial of given number is: %d",num2);
>>>>>>> 16c4f0275291b7acb2408f0fbfb078433fd4017a
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
<<<<<<< HEAD
                        printf("\n%d is not a prime number\n",num1);
                        goto out;
                    }
                printf("\n%d is a prime number",num1);
                out:
                printf("\npress enter to go back");
                scanf("%c");
                fflush(stdin);
=======
                        printf("%d is not a prime number\n",num1);
                        goto out;
                    }
                printf("%d is a prime number\n",num1);
                out:
>>>>>>> 16c4f0275291b7acb2408f0fbfb078433fd4017a
                break;
            case 3:
                printf("enter a number: ");
                scanf("%d",&num1);
                fflush(stdin);
                if (num1%2==0)
<<<<<<< HEAD
                    printf("\n%d is a even number\n", num1);
                else 
                    printf("\n%d is a an odd number\n",num1);
                printf("\npress enter to go back");
                scanf("%c");
                fflush(stdin);
=======
                    printf("%d is a even number\n", num1);
                else printf("%d id a an even number\n");
>>>>>>> 16c4f0275291b7acb2408f0fbfb078433fd4017a
                break;
            case 4:
                printf("\n**************************************");
                printf("\t\t---you have exited the prgram---");
<<<<<<< HEAD
                exit;
            default: 
                printf("invalid input, press enter to go back");
                scanf("%c");                  
=======
            default: 
                printf("invalid input, press enter to go back");
                scanf("%c");   
>>>>>>> 16c4f0275291b7acb2408f0fbfb078433fd4017a
            }
    } while (1);
}