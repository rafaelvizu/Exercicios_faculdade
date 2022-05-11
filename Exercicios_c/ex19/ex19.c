#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int vericarStrDecimal(char valor[30]) {
    for (int a=0; a<strlen(valor); a++) {
        if (isdigit(valor[a]) == 0)
        {
            return 0;
        } else if (a == strlen(valor)-1)
        {
            return 1;
        }
    }
}

int main() {
    char num_str[30];

    printf("Digite um valor: ");
    scanf("%s", &num_str);

    printf("\n");

    if (vericarStrDecimal(num_str)) {
        int num_int = atoi(num_str);
        for (int i = 0; i <= 10; i++)
        {
            printf("%d\tx\t%d\t=\t%d\n", num_int, i, (num_int * i));
        }
    } else {
        printf("\nValor invalido. Tente de novo!\n");
    }

    system("pause");
    return 0;
}