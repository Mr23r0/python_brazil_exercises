'''Faça um Programa que peça a temperatura em graus Celsius, 
   transforme e mostre em graus Fahrenheit.'''

celsius = input('Digite o valor em Celsius: ')
fahrenheit = float(celsius) * 9/5 + 32

print(f'O temperatura correspondente é: {fahrenheit:.1f}ºF')