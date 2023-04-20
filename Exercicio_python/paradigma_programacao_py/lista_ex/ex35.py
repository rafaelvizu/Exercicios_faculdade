conjunto = set()

while True:
     print('--' * 30)
     valor = int(input('Digite um valor (-1 para sair): '))

     if (valor == -1):
          break
     elif valor < 0 or valor > 1000:
          print('Valor inválido')
          continue
     
     conjunto.add(valor)


print(f'\n\nO menor número digitado foi {min(conjunto)} e o maior foi {max(conjunto)}')
print(f'A soma dos números digitados é {sum(conjunto)}')