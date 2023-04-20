notas = list()

for i in range(0, 4):
     nota = float(input(f'Digite a {i + 1}ª nota: '))
     notas.append(nota)

print(f'\n\nA média das notas é: {sum(notas) / len(notas):0.2f}')
