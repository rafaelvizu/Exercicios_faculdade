from random import randint

def gerarConjunto(n):
     conjunto = set()
     while len(conjunto) < n:
          conjunto.add(randint(0, 100))
          
     return conjunto

n = int(input('Digite a quantidade de números que deseja gerar: '))
conjunto = gerarConjunto(n)

print('--' * 30)
print(f'\nO menor número gerado foi {min(conjunto)} e o maior foi {max(conjunto)}')
print(f'A soma dos números gerados é {sum(conjunto)}')
