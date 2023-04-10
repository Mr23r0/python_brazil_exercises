''' Faça um Programa que peça dois números e imprima o maior deles'''
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

if n1.isnumeric(): 
    if (float(n1) > float(n2)):
        print(f'{n1} é maior.')
    elif (float(n2) > float(n1)):
        print(f'{n2} é maior')
    else:
        print('Eles são iguais')
else:
    print('Você não digitou apenas números')