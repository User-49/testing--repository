#include <stdio.h>

/*calculating grades based on marks input*/

void main(){
    int m1,m2,m3,m4,m5, marks;
    
    printf("enter marks of 5 subjects: \n");
    scanf("%d%d%d%d%d", &m1, &m2, &m3, &m4, &m5);
    
    marks =(m1+m2+m3+m4+m5)*0.2;
    
    if (marks>=60) printf("You got First dividion!!");
    if ((marks<60)&&(marks>=50)) printf("you got second division");
    if ((marks<50) && (marks>=40)) printf("you got second division");
    if (marks<40) printf("you failed, better luck next time...");
}