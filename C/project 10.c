#include <stdio.h>
#include <math.h>

/*to find area of tringly by lenghts of 3 sides*/
/*Area=√s(s−a)(s−b)(s−c)*/

int main(){
    float l1,l2,l3,s, area;
    printf("enter the sides of triangle: ");
    scanf("%f %f %f", &l1, &l2, &l3);
    s = (l1+l2+l3)/2;
    area =  sqrt(s*(s-l1)*(s-l2)*(s-l3));
    printf("area of trinagle is: %f\n", area);
    return 0;
}
