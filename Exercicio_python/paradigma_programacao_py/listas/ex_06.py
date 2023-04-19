# 6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor_da_hora = float(input('Valor da hora: R$'))
horas_trabalhadas = float(input('Digite quantas horas trabalhou esse mês: '))

salario_do_mes = valor_da_hora * horas_trabalhadas

print(f'\nSeu salário será de R${salario_do_mes:.2f}')
