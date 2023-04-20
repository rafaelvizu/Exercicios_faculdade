numeros = list()

for i in range(0, 5):
     numeros.append(int(input(f'Digite o {i + 1}º número: ')))

print(f'\nO maior número digitado foi: {max(numeros)}')
