''' Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
    arredonde os valores para cima, isto é, considere latas cheias'''

import math
tamanho_area = input('Informe o tamanho da area em metros quadrados: ')
litros_necessarios = float(tamanho_area) / 6
latas_necessarias = math.ceil(float(litros_necessarios) / 18)
preco_tot_latas = float(latas_necessarias) * 80.00
galoes_necessarios = math.ceil(float(litros_necessarios) / 3.6)
preco_tot_galoes = float(galoes_necessarios) * 25.00


print('=-'*25)
print(f'Situação 1:\n'\
      f'Para pintar {tamanho_area}m² você precisará de {latas_necessarias} lata(s) de tinta.\n'\
      f'Total da compra: R${preco_tot_latas:.2f}')
print(f'=-'*25)
print(f'Situação 2:\n'\
      f'Para pintar {tamanho_area}m² você precisará de {galoes_necessarios} galão(es) de tinta.\n'\
      f'Total da compra: R${preco_tot_galoes:.2f}')
print(f'=-'*25)
print(f'Situação 3:\n'\
      f'Para pintar {tamanho_area}m² você precisará de {...} latas e {...} galões de tinta.\n'\
      f'Total da compra: R${...}')