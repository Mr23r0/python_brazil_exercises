'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
   Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

genero = input('Informe o sexo [M]asculino [F]eminino: ').lower()
if (genero[0] == 'm'):
    print('Gênero identificado: Masculino')
elif(genero[0] == 'f'):
    print('Gênero identificado: Feminino')
else:
    print('Gênero inválido.')