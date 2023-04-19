# 2. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = list()

for i in range(0, 4):
    nota = float(input(f'Digite a nota do {i+1} semestre: '))
    notas.append(nota)

print(f'\nSua média foi de { (sum(notas) / 4):.2f }')
