caracteres = list()

for i in range(0, 10):
     caracteres.append(str(input("Digite um caractere: "))[0])

numero_de_consoantes = (caracteres.count('a') + caracteres.count('e') + 
                        caracteres.count('i') + caracteres.count('o') + 
                        caracteres.count('u'))

print(f"\n\nA quantidade de consoantes digitadas é: {numero_de_consoantes}")