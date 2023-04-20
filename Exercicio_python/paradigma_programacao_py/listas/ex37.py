def numPrimo(num):
     if numero < 0:
          num = num * -1

     # já que 1 e 2 são primos, não precisa testar
     # esse loop vai de 2 até num-1 (excluindo num)
     # se num for divisível por qualquer um desses
     # números, então não é primo
     for i in range(2, num):
          if num % i == 0:
               return False
          
     return True


numero = int(input('Digite um número: '))

if numero == 0:
     print('Zero é um valor indivisível')
     exit()

print('\n')

if numPrimo(numero):
     print(f'{numero} é um número primo')
else:
     print(f'{numero} não é um número primo')