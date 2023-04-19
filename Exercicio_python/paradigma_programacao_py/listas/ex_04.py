# 4. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from math import pi

raio = float(input('Digite o raio do circulo (em cm): '))
area = raio * (pi ** 2)

print(f'\nA área do circulo é igual a {area:.2f}cm²')

