#include <stdio.h>


int main() {
     char matricula[50];

     printf("Digite o numero de matricula: ");
     scanf("%s", matricula);

     printf("\n\nNumero de matricula: %s\n\n", matricula);

     char algorismo;

     printf("Digite um dos primeiros quatros algorismos da sua matricula: ");
     fflush(stdin);
     scanf("%c", &algorismo);


     float n1, n2;

     printf("\nDigite um numero: ");
     scanf("%f", &n1);

     printf("Digite mais um numero: ");
     scanf("%f", &n2);

     printf("\n");
     if (algorismo == matricula[3])
     {
          printf("Adicao: %0.1f", n1+n2);
     } else if (algorismo == matricula[1])
     { 
          printf("Subtracao: %0.1f", n1-n2);
     } else if (algorismo == matricula[4])
     {
          printf("Multiplicacao: %0.1f", n1*n2);
     } else if (algorismo == matricula[2]) {
          printf("Divisao: %0.1f", n1/n2);
     } else if (algorismo == matricula[0]) {
          printf("Exit...");
     }
     
     
     
     return 0;
}