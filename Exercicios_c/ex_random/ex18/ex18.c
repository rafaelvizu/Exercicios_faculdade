#include <stdio.h>
#include <stdlib.h>


int opcoes(int id_cadastro) {
    int selecao;
    while (0==0) {
        printf("\n\nESCOLHA O PRODUTO %d\n\n", (id_cadastro));
        printf("|1| - TRICO\n");
        printf("|2| - CROCHE\n");
        printf("|3| - PINTURA\n\n");
        printf("|4| - SAIR\n\nR: ");

        scanf("%d", &selecao);

        if (selecao >= 1 && selecao <= 4) {
            return selecao;
            break;
        } else {
            printf("\n\nVALOR INVALIDO. TENTE DE NOVO!\n\n");
        }
    }
}


int main() {
    const float CUSTO_HORA = 11.36;
    float maosDeObras[4], custos[4], valoresTotais[4], lucros[4];
    char *tiposProdutos[4] = {" ", " ", " ", " "};

    for (int i=0; i<4; i++) {
        int selecao = opcoes((i+1));

        if (selecao != 4) {
            int horasTrabalhadas = 0;

            printf("\nCUSTOS MATERIAIS: R$");
            scanf("%f", &custos[i]);

            printf("\nHORAS TRABALHADAS NA PECA: ");
            scanf("%d", &horasTrabalhadas);

            maosDeObras[i] = CUSTO_HORA * horasTrabalhadas;

            switch (selecao)
            {
            case 1:
                tiposProdutos[i] = "TRICO   ";
                lucros[i] = ((custos[i] + maosDeObras[i]) * 13) / 100;
                valoresTotais[i] = lucros[i] + maosDeObras[i] + custos[i];
                break;
            case 2:
                tiposProdutos[i] = "CROCHE  ";
                lucros[i] = ((custos[i] + maosDeObras[i]) * 11) / 100;
                valoresTotais[i] = lucros[i] + maosDeObras[i] + custos[i];
                break;
            case 3:
                tiposProdutos[i] = "PINTURA ";
                custos[i] /= 2;
                lucros[i] = ((custos[i] + maosDeObras[i]) * 10) / 100;
                valoresTotais[i] = lucros[i] + maosDeObras[i] + custos[i];
                break;
            }
        } else {break;}

    }
    printf("\n\n");

    if (tiposProdutos[0] != " ") {
        float lucroTotal;
        for (int i = 0; i < 4; i++)
        {
            if (tiposProdutos[i] != " ") {
                printf("PRODUTO %d\t", (i+1));
                printf("TIPO: %s\t", tiposProdutos[i]);
                printf("CUSTOS: R$%0.2f\t\t", custos[i]);
                printf("MAO DE OBRA: R$%0.2f\t\t", maosDeObras[i]);
                printf("VALOR TOTAL: R$%0.2f\n", valoresTotais[i]);

                lucroTotal += lucros[i];
            }
        }

        printf("\nO lucro total e de R$%0.2f. Descontando 5%% de imposto (R$%0.2f), ", lucroTotal, ((lucroTotal * 5) / 100));
        lucroTotal -= (lucroTotal * 5) / 100;
        printf("temos o lucro total igual a R$%0.2f\n", (lucroTotal));

        if (lucroTotal >= 200) {
            printf("\n\nVoce pode gastar R$%0.2f. Assim, vamos deixar R$%0.2f na conta poupanca", (lucroTotal/3), ((lucroTotal/3) * 2));
        } else if (lucroTotal < 200 && lucroTotal > 100) {
            printf("\n\nVoce podera gastar apenas R$%0.2f. Assim, vamos deixar R$%0.2f na conta poupanca", ((lucroTotal * 30)/ 100), (lucroTotal * 70) / 100);
        } else if (lucroTotal <= 100 && lucroTotal >= 0) {
            printf("\n\nVoce podera gastar apenas R$%0.2f. Assim, vamos deixar R$%0.2f na conta poupanca", ((lucroTotal*7.5) / 100), (lucroTotal - ((lucroTotal*7.5) / 100)));            
        }
        
    }

    printf("\n\n");
    system("pause");

    return 0;
}