temperaturas = list()

for i in range(0, 12):
     temperatura = float(input(f"Temperatura do mês {i + 1}: "))
     temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)

print(f"Média anual: {media:.2f}ºC")
