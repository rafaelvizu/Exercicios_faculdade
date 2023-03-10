from time import sleep
import os

def clear():
     os.system('cls' if os.name == 'nt' else 'clear')

def menu():
     print('CALCULADORA\n\n')

     print('1. Sumar')
     print('2. Subtrair')
     print('3. Multiplicar')
     print('4. Dividir')
     print('5. Resto')

     print('\n0. Sair')

     resp = str(input('\nEscolha uma opção: '))

     if (resp in ['1', '2', '3', '4', '5', '0']):
           return resp
     else: 
          clear()
          print('\nOpção inválida!')
          sleep(5)
          clear()
          return menu()
     