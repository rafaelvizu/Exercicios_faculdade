def entrada_vetor(vetor):
     for i in range(0, 10):
          print('=' * 40)
          vetor.append(int(input("Digite um valor: ")))
     return vetor

vetor_1 = list()
vetor_2 = list()

entrada_vetor(vetor_1)
print('\n')
entrada_vetor(vetor_2)


# intercalando
vetor_3 = list()
for i in range(0, 10):
     vetor_3.append(vetor_1[i])
     vetor_3.append(vetor_2[i])
     
print(f'\n\nVetor 3: {vetor_3}')
