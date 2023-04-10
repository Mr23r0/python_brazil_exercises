nome_aluno = input('Qual é o nome do aluno: ')
nota1 = input('Digite a nota do primeiro bimestre: ')
nota2 = input('Digite a nota do segundo bimestre: ')
nota3 = input('Digite a nota do terceiro bimestre: ')
nota4 = input('Digite a nota do quarto bimestre: ')
media = 0

if (nota1.isalpha() == True or nota2.isalpha() == True or nota3.isalpha() == True or nota4.isalpha() == True):
    print('Parece que você não digitou somente numeros ')

else:
    media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4
    print(f"A média do aluno(a) {nome_aluno} é {media}")