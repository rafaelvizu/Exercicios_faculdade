#include <stdio.h>


int main(){
    const float CONV_MBIT_MB = 0.125;
    float tam_download, velocidade_internet;

    printf("Tamanho do download: (MB) ");
    scanf("%f", &tam_download);

    printf("Velocidade da internet: (Mbit/1s) ");
    scanf("%f", &velocidade_internet);

    velocidade_internet = velocidade_internet * CONV_MBIT_MB;

    printf("\nO DOWNLOAD VAI DEMORAR %0.0fs PARA FINALIZAR...\n\n", (tam_download/velocidade_internet));

    return 0;
}