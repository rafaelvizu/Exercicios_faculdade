from math import prod

numeros = list()

for i in range(0, 5):
     numeros.append(int(input(f'Número {i + 1}: ')))

print('--' * 40)

print(f'A soma dos números é: {sum(numeros)}')
print(f'A multiplicação dos números é: {prod(numeros)}')
print(f'Os números digitados: {sorted(numeros)}')

print('--' * 40)