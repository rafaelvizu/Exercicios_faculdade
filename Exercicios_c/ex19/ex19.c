#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int count(char str[250], char caracter) {
	int cont = 0;
	for (int i=0; i<strlen(str); i++){
		if (str[i] == caracter) {
			cont++;
		}
	}
	return cont;
}

int vericarStrDecimal(char valor[250]) {
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
    char num_str[250];

    printf("Digite um valor: ");
    scanf("%s", &num_str);

    printf("\n");

    if (vericarStrDecimal(num_str)) {
        int num_int = atoi(num_str);
        for (int i = 0; i <= 10; i++)
        {
            printf("%d\tx\t%d\t=\t%d\n", num_int, i, (num_int * i));
        }
    } else if (count(num_str, '.') == 1){
        printf("Valor invalido. Digite um numero inteiro!\n");
    } else {
    	printf("Valor invalido. Tente novamente!\n");
	}

    system("pause");
    return 0;
}
