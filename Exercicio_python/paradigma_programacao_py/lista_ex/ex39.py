valores = list()

for i in range(0, 10):
     valor = int(input(f'Digite o {i + 1}º valor: '))
     valores.append(valor)

print(f'\nValores em ordem inversa: {valores[::-1]}')
