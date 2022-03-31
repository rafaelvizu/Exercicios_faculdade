#include <stdio.h>
#include <stdlib.h>


int main() {
    float valor, lucro;
    int porcentagemLucro;

    printf("Valor produto: R$");
    scanf("%f", &valor);

    if (valor<200) {
        lucro = (valor * 50) / 100;
        porcentagemLucro = 50;
    } else {
        lucro = (valor * 45) / 100;
        porcentagemLucro = 45;
    }

    printf("\nValor original: R$%0.2f\tLucro de %d%%: +R$%0.2f\t\tTotal = R$%0.2f\n\n", valor, porcentagemLucro, lucro, (valor+lucro));

    system("pause");
    
    return 0;
}