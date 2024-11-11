#include <stdio.h>

int func(int*);

void main(){
    int len;
    printf("enter thre length of array: ");
    scanf("%d",&len);
    int arr[len];
    printf("enter the values: ");
    for (int i=0;i<len;i++) scanf("%d",&arr[i]);
    printf("average of the array is: %d", func(arr));
}

int func(int arr[]){
    int avg=0, len = sizeof(arr)/sizeof(arr[0]);
    for (int i=0;i<len;i++) avg+=arr[i];
    return (avg/len);
}