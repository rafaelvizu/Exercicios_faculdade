#include <stdio.h>
#include <math.h>

int main() {
     int hora_chegada, minuto_chegada, hora_saida, minuto_saida;

     printf("Digite a hora de chegada: ");
     scanf("%d", &hora_chegada);

     printf("Digite o minuto de chegada: ");
     scanf("%d", &minuto_chegada);
     

     printf("\nDigite a hora de saida: ");
     scanf("%d", &hora_saida);

     printf("Digite o minuto de saida: ");
     scanf("%d", &minuto_saida);

     if (hora_chegada > hora_saida) {
          printf("\nNao trabalhamos 24h. Por favor digite um valor valido\n");
     } else {

          float horaChegadaF, horaSaidaF, valor = 0;

          horaChegadaF = ((float) minuto_chegada/60) + hora_chegada;
          horaSaidaF = ((float) minuto_saida/60) + hora_saida;


          int tempoEstacionamento = ceil(horaSaidaF-horaChegadaF), i;

          for (i = 1; i <= tempoEstacionamento; i++)
          {
          if (i<=2)
          {
               valor += 2;
          } else if (i>=3 && i<=4) {
               valor += 2.8;
          } else {
               valor += 3;
          }
          
          }

          printf("\n\nChegada: \t%d:%d\nSaida: \t\t%d:%d", hora_chegada, minuto_chegada, hora_saida, minuto_saida);
          printf("\nTempo total: \t%dh", tempoEstacionamento);
          printf("\nValor: \t\tR$%0.1f", valor);

     }
     
     return 0;
}