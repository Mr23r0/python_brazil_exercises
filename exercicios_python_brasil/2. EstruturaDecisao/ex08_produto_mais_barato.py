'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato.'''

produto1 = float(input('Informe o preço do primeiro produto: R$'))
produto2 = float(input('Informe o preço do segundo produto: R$'))
produto3 = float(input('Informe o preço do terceiro produto: R$'))
mais_barato = 0

if produto1 < produto2 and produto1 < produto3:
    mais_barato = f'Produto 1 que custa: R${produto1:.2f}'
elif produto2 < produto1 and produto2 < produto3:
    mais_barato = f'Produto 2 que custa: R${produto2:.2f}'
else:
    mais_barato = f'Produto 3 que custa: R${produto3:.2f}'

print(f'O mais barato é o {mais_barato}')