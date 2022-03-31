#include <stdio.h>
#include <math.h>


int main() {
	float r, a;
	
	printf("Raio do circulo: (cm) ");
	scanf("%f", &r);
	
	
	a = 3.14 * (pow(r, 2));
	
	printf("A area do circulo e %0.1fcm", a);
	
	return 0;
}
