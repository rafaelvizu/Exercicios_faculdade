#include <stdio.h>
#include <stdlib.h>


void horasMinuto(int min, int *minVarAddress, int *horVarAddress) {
     /*
          Aproveitando que o valor é arredondado em um divisão do tipo inteiro
     */

     *horVarAddress = min / 60;
     *minVarAddress = min - (*horVarAddress * 60);
}

int main() {
     int min, hor, minIn = 1;

     printf("\nDigite o total de minutos: ");
     scanf("%d", &minIn);

     horasMinuto(minIn, &min, &hor);
     printf("\n%dh:%dmin \n\n", hor, min);


     return 0;
}
