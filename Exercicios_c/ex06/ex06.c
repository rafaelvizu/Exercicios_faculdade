#include <stdio.h>
#include <stdlib.h>


int main() {
    float a, b, c;

    printf("Hipotenusa (a): ");
    scanf("%f", &a);

    printf("Cateto Adjacente (b): ");
    scanf("%f", &b);

    printf("Cateto Oposto (c): ");
    scanf("%f", &c);

    if ((b-c < a && a < b+c) && (a-c < b && b < a+c) && (a-b < c && c < a+b)) {
        printf("\nE um triangulo ");

        if (a == b && a == c && b == c) {
            printf("equilatero!");
        } else if ((a==b && c!=b) || (a==c && a!=c) || (b==c && b!=a)) {
            printf("isoceles!");
        } else if (a!=b && b!=c && c!=a) {
            printf("escaleno!");
        }
    } else {
        printf("\nNao e um triangulo!\n\n");
    }

    system("pause");

    return 0;
}