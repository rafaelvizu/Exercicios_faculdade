def seq_fib(n):
     a, b = 0, 1
     print('-' * 30)
     for i in range(0, n):    
          a, b = b, a + b
          print(a, end=' ')

num_termos = int(input('Digite o número de termos da sequência de Fibonacci: '))
seq_fib(num_termos)