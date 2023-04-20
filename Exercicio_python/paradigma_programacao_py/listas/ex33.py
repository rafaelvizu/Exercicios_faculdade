def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    

n = int(input('Digite um número: '))

print(f'\nO fatoração de {n} é {fatorial(n)}')
