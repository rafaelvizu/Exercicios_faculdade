pessoas = list()
pessoa = dict()

for i in range(0, 5):
     print(f'{"=" * 40}')
     pessoa['idade'] = int(input(f'Idade da {i + 1}ª pessoa: '))
     pessoa['altura'] = float(input(f'Altura da {i + 1}ª pessoa: '))

     pessoas.append(pessoa.copy())

print('--' * 40)
print(f'\nLista de pessoas')

pessoas = reversed(pessoas)

for pessoa in pessoas:
     print(f'\nIdade: {pessoa["idade"]} ano(s)')
     print(f'Altura: {pessoa["altura"]:0.2f}m')     
