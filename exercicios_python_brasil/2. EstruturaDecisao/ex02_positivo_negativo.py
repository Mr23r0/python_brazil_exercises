'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

valor = input('Informe um número: ')

if (valor.isnumeric() == True or '-' in valor):
    if(int(valor) > -1):
        print('O valor informado é positivo.')
    else:
        print('O valor informado é negativo.')
else:
    print('Você não digitou um número.')