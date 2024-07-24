# include <stdio.h>

void main(){
    int basic, hra, da;
    
    printf("Enter basic salary: ");
    scanf("%d", &basic);
    if (basic<1500)
    {hra = basic/10;da = basic*9/10;}
    else
    {hra = 500;da=basic*98/100;}
    
    printf("Gross salry of employee: %d", basic+hra+da);
        
}