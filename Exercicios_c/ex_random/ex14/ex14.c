#include <stdio.h>
#include <math.h>


int main() {
    float parede_m2, valorPagar;
    int qnt_latas;
    const VALOR_LATA = 80;

    printf("Tamanho da parede em metros quadrado: ");
    scanf("%f", &parede_m2);

    qnt_latas = (int) ceil((parede_m2 / 3/*Quantos litros vai usar*/) / 18);
    valorPagar = VALOR_LATA * qnt_latas;

    printf("\nVai precisar de %d latas de tintas, para uma parede de %0.1f metros quadrados. \nO valor final a se pagar e R$%0.2f", qnt_latas, parede_m2, valorPagar);
}