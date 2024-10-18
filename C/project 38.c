#include <stdio.h>
void main(){
int i=58,*j,**k;

j=&i;
k=&j;
printf("%u\n",&i);
printf("%u\n",j);
printf("%u\n\n",k);

printf("%d\n",*j);
printf("%u\n", **k);
}
