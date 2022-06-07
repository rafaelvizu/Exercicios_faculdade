#include <stdio.h>
#include <stdlib.h>


int main() {
   /*   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
    *   Crie um algoritimo que leia um numero e alerte se ele é menor que 50, igual, ou menor que 50*
    *                                                                                               *
    *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   */
    int num;

    printf("Digite um numero qualquer: ");
    scanf("%d", &num);

    printf("\n");
    if (num > 50) {
        printf("O numero %d eh maior que 50", num);
    } else if (num == 50) {
        printf("O numero %d eh igual a 50", num);
    } else {
        printf("O numero %d eh menor que 50", num);
    }

    printf("\n\n");

    system("pause");
    return 0;
}