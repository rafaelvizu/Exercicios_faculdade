#include <stdio.h>


int main() {
	float av1, av2, av3, av4, media;
	
	printf("AV1: ");
	scanf("%f", &av1);
	
	printf("AV2: ");
	scanf("%f", &av2);
	
	printf("AV3: ");
	scanf("%f", &av3);
	
	printf("AV4: ");
	scanf("%f", &av4);
	
	media = (av1+av2+av3+av4) / 4;
	
	printf("\n\nAV1\tAV2\tAV3\tAV4\n\n");
	printf("%0.1f\t%0.1f\t%0.1f\t%0.1f", av1, av2, av3, av4);
	printf("\n\n\tMEDIA: %0.1f", media);
	
	
	return 0;
}
