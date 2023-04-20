numeros = list()

for i in range(0, 5):
     numeros.append(int(input(f'Digite o {i + 1}º número: ')))

print(f'\n\nA soma dos números digitados é: {sum(numeros)}')
print(f'\nA média dos números digitados é: {sum(numeros) / len(numeros)}')
