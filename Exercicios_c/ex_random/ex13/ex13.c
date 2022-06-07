#include <stdio.h>


int main(){
    float ganhoPorHora;
    int horasTrabalhadas;

    printf("Quantos voce ganha por hora? ");
    scanf("%f", &ganhoPorHora);

    printf("\nQuantas horas voce trabalha por mes? ");
    scanf("%d", &horasTrabalhadas);

    printf("\n\nTrabalhando %d horas e ganhando R$%0.1f a cada hora, seu salario no fim do mes sera R$%0.1f\n", horasTrabalhadas, ganhoPorHora, (horasTrabalhadas*ganhoPorHora));


    return 0;
}