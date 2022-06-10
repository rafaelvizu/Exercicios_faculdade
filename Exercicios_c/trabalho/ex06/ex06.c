#include <stdio.h>

// variaveis globais
int totID = 0;
int id[100];
int senha[100];
float saldo[100] = {0};

// criar desenho
void logoBanco() {
     for (int i = 0; i < 16; i++)
     {
          if (i<=2) {
               printf("\n     *");
          } else if (i> 2 && i<=4) {
               printf("\n    ***");
          } else if (i>4 && i<=8) {
               printf("\n   *****");
          } else if (i>8 && i<= 16) {
               printf("\n  *******");
               if (i==12)
               {
                    printf("\n  *BANCO*");
               }
               
          }
     }
}

void criarConta() { // funcao responsavel para criar a conta
     int repVar = 0;
     while (repVar == 0)
     {
          int senhaRep;
          printf("\n\n\tID: %d", totID+1);
          printf("\n\nDigite uma senha numerica: ");
          scanf("%d", &senhaRep);

          if (senhaRep == 0)
          {
               printf("\n\nNao e permitido o valor 0 ser usado como senha\n\n");
          } else {
               do {
               char escolha;
               printf("\n\nID: %d\nSenha: %d", totID+1, senhaRep);
               printf("\n\nDeseja confirmar e criar a conta? (s/n) ");
               fflush(stdin);
               scanf("%c", &escolha);

               if (escolha == 's')
               {
                    senha[totID] = senhaRep;
                    id[totID] = totID+1;
                    totID++;
                    printf("\n\nConta criada com sucesso!\n\n");

                    // para sair do laco principal
                    repVar = 1;
                    break;
               } else if (escolha == 'n') {
                    printf("\n\nConta nao criada!\n\n");

                    // para sair do laco principal
                    repVar = 1;
                    break;
               } else {
                    printf("\n\nValor invalido. Tende novamente!\n");
               }
               

          } while(0==0);
          }
     }
     
}

int verificarConta(int idDigitado, int senhaDigitada) {
     if (senhaDigitada == 0) {
          return 0;
     } else {
     for (int i = 0; i < 100; i++)
     {
          if (id[i] == idDigitado && senhaDigitada == senha[i])
          {
               return 1;
          }         
     }

     return 0;
     }
}

void menuConta(int idConta) {
     idConta--;
     int escolha = 0;
     while (escolha!=4)
     {
          printf("--------------------------------------------------\n");
          printf("\n\nO que deseja fazer?\n");

          printf("\n[1]: Ver saldo");
          printf("\n[2]: Depositar");
          printf("\n[3]: Sacar");
          printf("\n\n[4]: Sair\n\nR: ");

          scanf("%d", &escolha);

          float valor;
          switch (escolha)
          {
          case 1:
               printf("\nSaldo atual:\t R$%0.2f\n\n", saldo[idConta]);
               break;
          case 2:
               printf("\n\nValor que deseja depositar: R$");
               scanf("%f", &valor);

               if (valor>=0)
               {
                    saldo[idConta] += valor;
                    printf("\nValor de %0.2f depositado com sucesso!\n\n", valor);
               } else {
                    printf("\nValor invalido. Tende novamente!\n\n\n");
               }
               break;
          case 3:
               printf("Digite o valor ira sacar: R$");
               scanf("%f", &valor);

               if (valor < saldo[idConta]) 
               {
                    saldo[idConta] -= valor;
                    printf("\nValor de %0.2f sacado com sucesso!\n\n", valor);
               } else {
                    printf("\nValor invalido. Tende novamente!\n\n");
               }
               break;
          case 4:
               printf("\nVoltando para o menu...\n\n\n\n");
               break;
          default:
               printf("\n\nValor invalido!\n\n\n");
               break;
          }
     }
     
}


void acessarConta() {
     int senhaConta, idConta;

     printf("\nID: ");
     scanf("%d", &idConta);

     printf("Senha: ");
     scanf("%d", &senhaConta);

     if (verificarConta(idConta, senhaConta))
     {
          printf("\n\nLoggado com sucesso!\n\n");
          menuConta(idConta);
     } else {
          printf("\n\nDados invalidos!\n");
     }
     
}



int main() {
     logoBanco();
     
     int escolha=0;
     while (escolha!=3)
     {
          printf("--------------------------------------------------\n");
          printf("O que deseja fazer?\n\n");
          printf("[1]: Acessar conta\n");
          printf("[2]: Criar conta\n");
          printf("[3]: Sair\n\nR: ");

          scanf("%d", &escolha);
          switch (escolha)
          {
          case 1:
               acessarConta();
               break;
          case 2:
               criarConta();
               break;
          case 3:
               printf("\n\nSaindo...\n\n");
               break;
          
          default:
               printf("\n\nValor invalido. Tende novamente!\n");
               break;
          }
     }    
     return 0;
}
