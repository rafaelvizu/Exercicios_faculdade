sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

if sexo in ('M', 'F'):
    print(f'\nVocê é do sexo {( "masculino" if sexo == "M" else "feminino" )}')
else:
     print('\nSexo inválido')
