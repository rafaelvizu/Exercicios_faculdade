from random import randint

def gerar_alunos():
     alunos = list()

     for i in range(0, 10):
          aluno = dict()

          aluno['altura'] = randint(150, 200) / 100
          aluno['idade'] = randint(10, 18)

          alunos.append(aluno.copy())

     return alunos


alunos = gerar_alunos()

media = 0
qnt_fora_da_media = 0
for aluno in alunos:
     media += aluno['altura']

media = media / len(alunos)

for aluno in alunos:
     if aluno['altura'] < media and aluno['idade'] > 13:
          qnt_fora_da_media += 1

print(f"\n\nA média de altura dos alunos é: {media:0.2f}m")
print(f"A quantidade de alunos com altura abaixo da média e idade acima de 13 anos é: {qnt_fora_da_media}")
