'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
lista = [n1, n2, n3]
lista.sort(reverse=True)

print(lista)
