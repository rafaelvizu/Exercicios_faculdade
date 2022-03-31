#include <stdio.h>


int main() {
    const int PORC_INSS = 8, PORC_SINDICATO = 5;
    float salario, valorINSS, valorSindicado, valorPorHora;
    int horasTrabalhadas;

    printf("Quantos ganhas por hora? ");
    scanf("%f", &valorPorHora);

    printf("Quantas horas voce trabalha? ");
    scanf("%d", &horasTrabalhadas);

    salario = valorPorHora * horasTrabalhadas;

    valorINSS = (salario*PORC_INSS) / 100;
    valorSindicado = (salario*PORC_SINDICATO) / 100;

    printf("\n\nO salario inicial e R$%0.2f.\n", salario);

    salario -= (valorINSS+valorSindicado);

    printf("Descontando os valores do INSS (-R$%0.2f) e do sindicato (-R$%0.2f), o salario final fica igua a R$%0.2f\n", valorINSS, valorSindicado, salario);
}