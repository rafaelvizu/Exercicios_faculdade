#include <stdio.h>
#include <stdlib.h>


int main() {
   /*   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
        Crie um algoritmo que leia tres notas, calcule media e informe se o aluno foi aprovado  *
    *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   */
    float av1, av2, av3, media;

    printf("Nota 1: ");
    scanf("%f", &av1);
    
    printf("Nota 2: ");
    scanf("%f", &av2);

    printf("Nota 3: ");
    scanf("%f", &av3);

    media = (av1 + av2 + av3) / 3;

    printf("| Nota 1: %0.1f\t| Nota 2: %0.1f\t| Nota 3: %0.1f |\n", av1, av2, av3);
    printf("\n| Media: %0.1f\t| Situacao: %s |\n\n", media, ((6<=media)?"Aprovado":"Reprovado"));

    system("pause");
    return 0;
}