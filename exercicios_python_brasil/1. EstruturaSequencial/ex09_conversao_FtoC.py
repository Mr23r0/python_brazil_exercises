'''Faça um Programa que peça a temperatura em graus Fahrenheit, 
    transforme e mostre a temperatura em graus Celsius.'''

fahrenheit = input('Digite a temperatura em Fahrenheit: Fº')
celsius = (float(fahrenheit) - 32) * 5/9

print(f'O valor correpondente a: {celsius:.1f}ºC')