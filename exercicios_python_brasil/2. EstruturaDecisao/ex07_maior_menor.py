'''Faça um Programa que leia três números e mostre o maior e menor deles.'''

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
maior = 0
menor = 0

if n1 > maior:
    maior = n1
    if n2 < n3:
        menor = n2
    else:
        menor = n3

if n2 > maior:
    maior = n2
    if n1 < n3:
        menor = n1
    else:
        menor = n3

if n3 > maior:
    maior = n3
    if n2 < n1:
        menor = n2
    else:
        menor = n1


print(f'Maior: {maior}, menor: {menor}')