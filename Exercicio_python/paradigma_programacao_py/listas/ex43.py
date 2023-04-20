alunos = list()
aluno = dict() 

for i in range(0, 10):
     print('-' * 30)
     
     aluno['nota 1'] = float(input(f'Nota 1 do aluno {i + 1}: '))
     aluno['nota 2'] = float(input(f'Nota 2 do aluno {i + 1}: '))
     aluno['nota 3'] = float(input(f'Nota 3 do aluno {i + 1}: '))
     aluno['nota 4'] = float(input(f'Nota 4 do aluno {i + 1}: '))
     aluno['media'] = (aluno['nota 1'] + aluno['nota 2'] + aluno['nota 3'] + aluno['nota 4']) / 4
     alunos.append(aluno.copy())

print('-' * 30)
for i in range(0, len(alunos)):
     if alunos[i]['media'] >= 7:
          print(f"Aluno {i + 1} aprovado com média {alunos[i]['media']:.2f}")