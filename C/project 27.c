#include <stdio.h>
int class, subjects;
char;
void main(){
    while (11){
        printf("\nEnter the class obtained: ");
        scanf("%d",&class);
        printf("Enter number of subjects failed: ");
        scanf("%d",&subjects);
        
        switch (class){
            case 1:
                (subjects<=3?printf("\ntotal grace marks: %d",subjects*5):printf("\nTotal grace marks: 0"));
                break;
            case 2:
                (subjects<=2?printf("\ntotal grace marks: %d",subjects*4):printf("\nTotal grace marks: 0"));
                break;
            case 3:
                (subjects<=1?printf("\ntotal grace marks: %d",5):printf("\nTotal grace marks: 0"));
                break;
            default:
                printf("\nInvalid input");
                printf("\npress enter to go back");
        }
    }
}