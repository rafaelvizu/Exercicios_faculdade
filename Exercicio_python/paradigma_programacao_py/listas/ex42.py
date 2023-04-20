num_pares = list()
num_impares = list()
num_numeros = list()

for i in range(0, 20):
     num = int(input(f'Número {i + 1}: '))
     num_numeros.append(num)

     if num % 2 == 0:
          num_pares.append(num)
     else:
         num_impares.append(num)

print(f'\nNúmeros pares: {num_pares}')
print(f'Números ímpares: {num_impares}')
print(f'Números: {num_numeros}')
