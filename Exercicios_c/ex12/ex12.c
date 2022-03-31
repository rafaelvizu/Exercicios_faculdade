#include <stdio.h>
#include <math.h>


int main() {
    float l;

    printf("Valor de um dos lados do quadrado: (cm) ");
    scanf("%f", &l);

    printf("\nO valor da area do quadrato e %0.2fcm", pow(l, 2));

    return 0;
}