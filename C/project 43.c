#include <stdio.h>

void func(int *x){
for (int i=0;i<10;i++) printf("%u\n",*(x + i));
}


void main(){
int arr[5][2]={1,1,1,2,1,3,1,4,1,5};
func(arr);

for (int i=0;i<5;i++)printf("%u\n",*(arr+i));
}
