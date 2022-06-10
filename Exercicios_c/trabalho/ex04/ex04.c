#include <stdio.h>


int main() {
     int arrNum[4][2];
     int maior, menor;
     int posMaior[2];
     int posMenor[2];

     for (int i = 0; i < 4; i++)
     {
          printf("\nLinha: %d\n\n", i);
          for (int f = 0; f < 2; f++)
          {
               printf("Digite o valor [%d][%d]: ",i,f);
               scanf("%d", &arrNum[i][f]);

               if (i==0)
               {
                    menor = arrNum[i][f];
                    maior = arrNum[i][f];
                    posMaior[0] = i; posMaior[1] = f;
                    posMenor[0] = i; posMenor[1] = f;
               } else if (arrNum[i][f] > maior) {
                    maior = arrNum[i][f];
                    posMaior[0] = i; posMaior[1] = f;
               } else if (arrNum[i][f] < menor) {
                    menor = arrNum[i][f];
                    posMenor[0] = i; posMenor[1] = f;
               }
               
          }
          printf("\n");
     }


     printf("\n\nMaior:\t\t %d", maior);
     printf("\nPosicao:\t [%d][%d]\n\n", posMaior[0], posMaior[1]);

     printf("Menor:\t\t %d", menor);
     printf("\nPosicao:\t [%d][%d]", posMenor[0], posMenor[1]);
     

     return 0;
}