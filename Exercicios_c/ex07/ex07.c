#include <stdio.h>
#include <stdlib.h>


int main() {
    float d, km_combustivel;

    printf("Qual a distancia do percurso? (Km) ");
    scanf("%f", &d);

    printf("Quantos km o carro faz por litro? (Km/1L) ");
    scanf("%f", &km_combustivel);

    printf("\nO carro gastou %0.1f litro(s) de combustivel\n\n", (d / km_combustivel));


    system("pause");

    return 0;
}
