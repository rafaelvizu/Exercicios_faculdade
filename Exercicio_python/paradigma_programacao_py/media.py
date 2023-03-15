import modules

def media(nota1, nota2):
    return (nota1 + nota2) / 2


modules.clear()


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = media(nota1, nota2)


if media >= 6:
     print(f'Aprovado: {media:.2f}')
else:
     print(f'Reprovado: {media:.2f}')
