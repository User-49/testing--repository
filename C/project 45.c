#include <stdio.h>
#include <stdlib.h>

int determinant(int *,int);
void input(int *,int,int);
void display(int *,int,int);
void multiply(int *,int *,int *,int,int,int,int);
void scalar_multiply(int *,int ,int);
void add(int *,int *,int *,int);
void adjoint(int *,int,int);
void substract(int *,int *,int *,int);

void main(){

	int m1,n1,choice=0,*arr_3_ptr=NULL;

	start:
	printf("------------------------------------------------------------------------\n");
	
	printf("enter the dimentions of matrix(MxN): ");
	if (scanf("%dx%d",&m1,&n1)!=2){
		printf("invalid values\n");
		goto start;
	}
	int *arr_1=malloc(m1*n1*sizeof(int));
	printf("\n");
	input(arr_1, m1, n1);
	
	do{
		printf("------------------------------------------------------------------------\n\n");
		
		printf("operand matrix:\n\n");
		display(arr_1,m1,n1);

		printf("\nwhat do you wish to do..?\n");
		printf("1.add matrix\n");
		printf("2.substract matrix\n");
		printf("3.multiply matrix\n");
		printf("4.invert matrix\n");
		printf("5.determinant of matrix\n");
		printf("6.multiply by scalar\n");
		printf("7.enter a new matrix\n");
		printf("0.exit\n");

		printf("\nenter choice: ");
		scanf("%d",&choice);

		switch (choice){
			case 1:
				int arr_2[m1*n1],*arr_3=malloc(m1*n1*sizeof(int));
				arr_3_ptr=arr_3;
				printf("\nenter the matrix:\n\n");
				input(arr_2,m1,n1);
				add(arr_1,arr_2,arr_3,m1*n1);
				break;
			case 2:
				break;
			case 3:
				break;
			case 4:
				break;
			case 5:
				break;
			case 6:
				break;
			case 7:
				break;
			case 0:
				printf("you have exited the program\n");
				break;
			default:
				printf("invalid input\n");

		}



	}while (choice);

	printf("************************************************************************\n");
}



void input(int *arr,int m,int n){
	for (int i=0; i<m; i++){
		printf("enter the elements of row %d: ",i+1);
		for (int j=0; j<n; j++)
			scanf("%d", (arr+i*n+j));
	}
}


void display(int *arr,int m,int n){
	for (int i=0; i<m; i++){
	printf("[\t");
	for (int j=0; j<n; j++)
		printf("%d\t", *(arr+i*n+j));
	printf("]\n");
	}
}


void add(int *arr_1,int *arr_2,int *arr_3,int len){
	for (int i=0;i<len;i++)
		(*(arr_3+i))=(*(arr_1+i))+(*(arr_2+i));
}


void substract(int *arr_1,int *arr_2,int *arr_3,int len){
	for (int i=0;i<len;i++)
		(*(arr_3+i))=(*(arr_1+i))-(*(arr_2+i));
}


void multiply(int *arr_1,int *arr_2,int *arr_3,int m1,int n1,int n2,int len){
	for (int i=0;i<len;i++){
		*(arr_3+i)=0;
		for (int j=0;j<n1;j++)
			*(arr_3+i)+=*(arr_1+(i/m1)*n1+j)*(*(arr_2+(i%n2)+j*n2));
	}
}

/*
int determinant(int *arr_1,int s){
	if (s==1)
		return (*arr_1);
	else{
		int arr[(s-1)*(s-1)];
		for (int i=0;i<s*s;i++){
			if ()
		}
	}
}
*/

void scalar_multiply(int *arr_1,int len, int num){
	for (int i =0;i<len;i++)
		*(arr_1+i) *= num;
}