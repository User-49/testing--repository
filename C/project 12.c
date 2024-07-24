#include <stdio.h>

/*giving discount if number of items purchased is more than 1000*/

void main(){
    int price, quantity;
    printf("enter number of items purchased:");
    scanf("%d", &quantity);
    printf("enter total price of items: ");
    scanf("%d", &price);
    if (quantity>1000)
    {
        price -= price/10;
        printf("idea works");
    }
    printf("final price of products: %d", price);
    
}