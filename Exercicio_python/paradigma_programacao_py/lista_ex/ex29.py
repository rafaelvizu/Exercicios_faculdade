def intervalo(v1, v2):
     a = list()
     if v1 > v2:
          for i in range(v2+1, v1):
               a.append(i)
               
     else:
          for i in range(v1+1, v2):
               a.append(i)
                    
     return a.copy()


v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))


print(f'\n\nOs valores entre {v1} e {v2} são: {intervalo(v1, v2)}')
print(f'\nA soma dos valores entre {v1} e {v2} é: {sum(intervalo(v1, v2))}')
