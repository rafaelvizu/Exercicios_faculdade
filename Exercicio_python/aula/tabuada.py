from modules import clear
from time import sleep

def main():
     clear()
     print('Tabuada'.center(30, '-'), end='\n\n\n')
     num = int(input('Digite um valor: '))
     clear()

     for i in range(1, 11):
          print(f'{num} x {i} = {num * i}')

     
     resp = input('\n\nDeseja continuar? [S/N] ').upper().strip()[0]
     clear()

     if resp == 'N':
          print('Obrigado por usar o programa!')
          exit()
     elif resp != 'S':
          print('Opção inválida!')
          sleep(2)


     return main()


main()
