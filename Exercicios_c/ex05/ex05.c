#include <stdio.h>
#include <stdlib.h>


int main() {
    float valor, lucro;

    printf("Valor produto: R$");
    scanf("%f", &valor);

    if (valor<200) {
        lucro = (valor * 50) / 100;
    } else {
        lucro = (valor * 45) / 100;
    }

    printf("\nValor original: R$%0.2f\tLucro: +R$%0.2f\t\tTotal = R$%0.2f\n\n", valor, lucro, (valor+lucro));

    system("pause");
    
    return 0;
}