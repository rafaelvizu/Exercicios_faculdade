from random import randint

resultado_dado = list()

for i in range(0, 100):
    resultado_dado.append(randint(1, 6))

for valor in range(1, 7):
     print(f"Valor {valor} = {resultado_dado.count(valor)} veze(s)")
