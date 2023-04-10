'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
import math
tamanho_area = input('Qual o tamanho da area em metros quadrados a ser pintada: ')
litros_tinta = float(tamanho_area) / 3
qtd_de_latas = math.ceil(float(litros_tinta) / 18)
preco_final = qtd_de_latas * 80.00
print('=-'*25)
print(f'Para pintar {tamanho_area}m² você precisará de {qtd_de_latas} lata(s) de tinta\n'
      f'Preço total da compra: R${preco_final:.2f}')
print('=-'*25)