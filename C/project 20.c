#include <stdio.h>

void main(){
    int n,m;
    char x;

    printf("Enter the value of n:");
    scanf("%d",&n);

    for (;n;n--)
    {
        m=n;
        for (x='A';m;x+=1,m--)
        {
            printf("%c",x);
        }
        printf("\n");
    }
    scanf("%d");
}
