#include <stdio.h>


int main() {
	float valor;
	
	printf("Valor em metros: ");
	scanf("%f", &valor);	
	
	printf("\n\n Convertendo %0.1fm para %0.1fcm", valor, (valor*100));
	
	return 0;
}
