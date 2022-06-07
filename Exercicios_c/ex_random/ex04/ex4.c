#include <stdio.h>
#include <stdlib.h>


void aplicarDesconto(float valor, int desconto) {
    float descontoValor = (valor*desconto) / 100;

    printf("\nValor original: R$%0.2f\n", valor);
    printf("Desconto de %d%%: -R$%0.2f\n", desconto, descontoValor);
    printf("Valor final: R$%0.2f\n", (valor-descontoValor));
}

int main() {
    while (0 == 0)
    {
        float valor;

        printf("---------------------------------\n");
        printf("Digite o valor do produto (0 para fechar): R$");
        scanf("%f", &valor);

        fflush(stdin);
        
        if (valor==0) {
            printf("\nSaindo...\a\n\n");
            break;
        }
        else if (valor<0) {
            printf("\n\aValor negativo. Tente novamente!\n\n");
            continue;
        } 

        int repContinue = 1;
        while (repContinue == 1) {
            int formaPagamento;

            printf("\nDINHEIRO - DESCONTO: 10%%\tPIX - DESCONTO: 15%%\tCARTAO - DESCONTO: 0%%\n");

            printf("\nFORMA DE PAGAMENTO\n");
            printf("\n|1| - PIX\n|2| - DINHEIRO\n|3| - CARTAO\n\n|0| - Voltar\n\nR: ");
            scanf("%d", &formaPagamento);

            switch (formaPagamento)
            {
            case 1:
                aplicarDesconto(valor, 15);
                repContinue = 0;
                break;
            case 2:
                aplicarDesconto(valor, 10);
                repContinue = 0;
                break;
            case 3:
                aplicarDesconto(valor, 0);
                repContinue = 0;
                break;
            case 4:
                repContinue = 0;
                break;
            default:
                printf("\nValor invalido. Tente novamente!\a\n\n");
                break;
            }
        }
        return 0;

    }
    
}