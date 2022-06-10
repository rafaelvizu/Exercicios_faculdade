#include <stdio.h>


int main() {
     for (int i = 0; i < 16; i++)
     {
          if (i<=2) {
               printf("\n     *");
          } else if (i> 2 && i<=4) {
               printf("\n    ***");
          } else if (i>4 && i<=8) {
               printf("\n   *****");
          } else if (i>8 && i<= 16) {
               printf("\n  *******");
               if (i==12)
               {
                    printf("\n  *BANCO*");
               }
               
          }
     }

     
     
     

     return 0;
}