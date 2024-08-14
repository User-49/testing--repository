#include <stdio.h>
#include <math.h>

/*calculating sum of square of sine and cos of given degree angle */

void main() {
    float a,b;
    printf("enter two angles in degrees: ");
    scanf("%f%f", &a, &b);
    
    a = a/3.14; b=b/3.14;
    
    printf("square of sine nd cosine of this angle %f", pow(sin(a),2) + pow(cos(b),2));
}