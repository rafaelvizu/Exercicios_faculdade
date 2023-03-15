from modules.menu import menu, clear
import modules.operacoes as op


def main(valor=False):
    resp = menu()

    if resp == 0:
        exit()
    
    clear()

    if valor != False:
        n1 = valor
    else:
        n1 = int(input('Digite um número: '))

    n2 = int(input('Digite um número: '))

    resp = int(resp)

    if resp == 1:
        valor = op.somar(n1, n2)
    elif resp == 2:
        valor = op.subtrair(n1, n2)
    elif resp == 3:
        valor = op.multiplicar(n1, n2)
    elif resp == 4:
        valor = op.dividir(n1, n2)
    else:
        valor = op.resto(n1, n2)

    clear()
    print(f'O resultado é: {valor}')


    while True:
        resp = input('\n\nDeseja continuar? [S/N] ').strip().upper()[0]
        
        if resp == 'S':
            main(valor)
        elif resp == 'N':
            exit()


main()