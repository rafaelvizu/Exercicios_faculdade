from time import sleep


def fatorial(n):
     if n == 0:
          return 1
     else:
          return n * fatorial(n - 1)
    

while True:
     print('-' * 30)
     n = int(input('\nDigite um número (0 para sair): '))

     if n == 0:
          break    
     elif n < 0:
          print('O número deve ser positivo!')
          continue
     elif n >= 16:
          print('O número deve ser menor que 16!')
          continue
     
     print(f'\nO fatoração de {n} é {fatorial(n)}')


print('\n\n<3')