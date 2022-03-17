#include <stdio.h>
#include <stdlib.h>


int main() {

   /*   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
        Crie um algoritmo que leia um numero inteiro e informe se ele eh divisivel por 8    *
   *    *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   */
    int num;

    printf("Digite um numero inteiro: ");
    scanf("%d", &num);

    if (num%8 == 0) {
        printf("Ele eh divisivel por 8");
    } else {
        printf("Nao eh divisivel por 8");
    }


    return 0;
}