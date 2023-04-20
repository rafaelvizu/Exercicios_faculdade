def entrada_vetor(vetor):
     for i in range(0, 10):
          print('=' * 40)
          vetor.append(int(input(f'Valor {i+1}: ')))


vetor_1 = list()
vetor_2 = list()
vetor_3 = list()

entrada_vetor(vetor_1)
print('\n')
entrada_vetor(vetor_2)
print('\n')
entrada_vetor(vetor_3)


# intercalando
vetor_4 = list()
for i in range(0, 10):
     vetor_4.append(vetor_1[i])
     vetor_4.append(vetor_2[i])
     vetor_4.append(vetor_3[i])


print(f'\n\nVetor 4: {vetor_4}')