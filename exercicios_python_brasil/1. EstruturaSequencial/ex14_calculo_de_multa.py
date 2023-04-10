'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
adequadas.'''

peso_peixes = input('Informe o peso de peixes em kilos: ')
max_permitido = 50
multa_por_kilo = 4.00
excesso = 0
valor_multa = 0

if (float(peso_peixes) > 50):
    excesso = float(peso_peixes) - max_permitido
    valor_multa = multa_por_kilo * excesso
    print(f'Você excedeu {excesso:.2f}kg acima do limite, portanto deve pagar a multa de R${valor_multa:.2f}')
else:
    print('O peso está dentro do limite estabelecido.')
