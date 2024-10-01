#include <stdio.h>
void main(){
char l[]={1,4,3,4,4,4,6};
for (int i=0;i!=7;i++){
  int flag=0;
  for (int j=0;j<i;j++){
    if (l[i]==l[j]){
      flag=1;
      break;
      }
  }
  if (flag==0) printf("%d",l[i]);
}
printf("\n");
}
