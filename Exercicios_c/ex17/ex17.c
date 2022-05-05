#include <stdio.h>
#include <string.h>

char conferirDados() {
    while (0 == 0)
    {
        char escolha;

        printf("\n----------------------------------------");
        printf("\n\nOs dados estao correto? [s/n] ");
        fflush(stdin);
        scanf("%c", &escolha);
        printf("\n----------------------------------------\n");

        escolha = toupper(escolha);

        if (escolha == 'S' || escolha == 'N') {
            return escolha;
        }
    }
    
}

int main() {
    while (0 == 0)
    {
        char nome[400] = "";
        int idade, numParcelas;
        float valorEmprestimo, salarioCliente;

        while (0 == 0)
        {
            printf("Digite o nome do cliente: ");
            fflush(stdin);
            gets(nome);

            printf("Digite a idade do cliente: ");
            fflush(stdin);
            scanf("%d", &idade);

            if (nome != "" && idade>0) {
                printf("\nNOME: %s   \tIDADE: %d", nome, idade);
                char opcao = conferirDados();

                if (opcao == 'S')
                {
                    printf("\nDados cadastrados com sucesso!\n\n\n");
                    break;
                } else {
                    printf("\nDados nao cadastrados!\n\n\n");
                }
                
            }
        }

        if (idade < 18) {
            printf("\nVoce ainda e menor que 18 anos, sendo assim, nao podemos realizar emprestimos ao senhor!\n\n");
            break;
        } else {
            while (0 == 0)
            {
                printf("\nQual o seu salario: R$");
                scanf("%f", &salarioCliente);

                printf("Qual o valor do emprestimo: R$");
                scanf("%f", &valorEmprestimo);

                printf("\nEm quantas parcelas deseja pagar");
                scanf("%d", &numParcelas);

                if (numParcelas >= 1 && valorEmprestimo > 0 && salarioCliente > 0) {
                    break;
                } else {
                    printf("\n\nValores incorretos. Tente de novo!");
                }
            }

            printf("\n\nSALARIO: R$%0.2f  \tNUMERO DE PARCELAS: %d    \tVALOR DO EMPRESTIMO: R$%0.2f\n\n", salarioCliente, numParcelas, valorEmprestimo);
            
        }
    }

    return 0;
}