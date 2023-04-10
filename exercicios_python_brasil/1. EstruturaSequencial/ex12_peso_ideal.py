'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que 
   calcule seu peso ideal, usando a
   seguinte fórmula: (72.7*altura) - 58'''

altura = input('Digite a altura em metros: ')
peso_ideal = 72.7 * float(altura) - 58

print('Seu peso ideal seria: {:.2f}kg'.format(peso_ideal))