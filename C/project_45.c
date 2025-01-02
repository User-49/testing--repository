#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int m,n,*matrix;
double det(int*,int);

int main(){
start:
printf("\nenter the dimentions of the matrix(MxN): ");
if (scanf("%dx%d",&m,&n)!=2 || m!=n){
	printf("\n--invalid input--");
	goto start;}
matrix=(int*)malloc(sizeof(int)*m*n);
for (int i=0;i<m;i++){
	printf("enter elements of row %d: ",i+1);
	for (int j=0;j<n;j++)
		scanf("%d",(matrix + i*m + j));
}
printf("\ndeterminant of the given matrix: %f",det(matrix,n));
return 0;
}

double det(int *matrix,int n){
double det_val=0;
if (n==1) return *matrix;

int *arr=(int*)malloc(sizeof(int)*(n-1)*(n-1));
for (int i=0;i<n;i++){
	for (int j=n,k=0,x=n*n;j<x;j++){
		if (j%n==i) continue;
		*(arr+k)=*(matrix+j);
		printf("%d",*(arr+k));
		k++;
	}
	det_val += *(matrix+i)*det(arr,n-1)*pow(-1,i);
}
free(arr);
return det_val;
}
