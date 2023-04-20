qnt_numeros_pares = 0
qnt_numeros_impares = 0

for i in range(0, 10):
     numero = int(float(input(f'Digite o {i + 1}º número: ')))
     if numero % 2 == 0:
          qnt_numeros_pares += 1
     else:
          qnt_numeros_impares += 1


print(f'\n\nForam digitados {qnt_numeros_pares} números pares e {qnt_numeros_impares} números ímpares')