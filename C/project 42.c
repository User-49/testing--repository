#include <stdio.h>
void main(){
int l[]={1,1,2,2,2,3,4,5,3,4,5,2,1};
int a=l[0],b,flag;
for (int i=0;i<13;i++){

	int freq=0,flag=0;
	for (int j=0;j<13;j++)
		if (a==l[j]) freq++;
	printf("frequency of %d is: %d\n",a,freq);

	b=a;
	for (int k=1;k<13;k++)
		if ((a>l[k])&&(a>b)) {a=l[k];}
	}
}
