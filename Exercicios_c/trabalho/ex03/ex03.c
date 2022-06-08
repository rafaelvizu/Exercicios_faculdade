#include <stdio.h>


int main() {
     char *matricula;

     printf("Digite o numero de matricula: ");
     scanf("%s", matricula);

     printf("\n\nNumero de matricula: %s\n\n", matricula);

     char *algorismo;

     printf("Digite um dos quatros algorismos da sua matricula: ");
     scanf("%s", &algorismo);
     
     if (algorismo == matricula[3])
     {
          /* code */
     } else if (algorismo == matricula[1])
     {
          /* code */
     } else if (algorismo == matricula[4])
     {
          /* code */
     }
     
     
     
     return 0;
}