#include <stdio.h>


int main () {
     // valores
     int n[] = {1, 4, 5, 1, 5, 2, 5, 4, 5, 1 ,6, 5 , 34, 1, 54};
     int m[] = {4, 54, 4, 2, 4, 42, 23 ,42, 2, 4, 42, 2, 4 ,1 ,4};
     int x = 0;

     // for para passar pelas 15 posicoes do arr
     for (int i = 0; i < 15; i++)
     {
          x += n[i]*m[i]; // calculando produto escalar
     }
     
     // output
     printf("O pruduto escalar e igual a %d", x);

     return 0;
}