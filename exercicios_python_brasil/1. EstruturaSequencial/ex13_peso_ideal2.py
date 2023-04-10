'''Tendo como dado de entrada a altura (h) de uma pessoa, construa 
   um algoritmo que calcule seu peso ideal, utilizando as
   seguintes fórmulas:
     a. Para homens: (72.7*h) - 58
     b. Para mulheres: (62.1*h) - 44.7'''

altura = input('Digite sua altura em metros: ')
peso_ideal_homem = 72.7 * float(altura) - 58
peso_ideal_mulher = 62.1 * float(altura) - 44.7
print(f'O peso ideal para essa altura em homens seria: {peso_ideal_homem:.2f}kg\n'\
      f'O peso ideal para essa altura em mulheres seria: {peso_ideal_mulher:.2f}kg')