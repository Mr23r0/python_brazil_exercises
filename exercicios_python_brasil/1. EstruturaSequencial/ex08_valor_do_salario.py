''' Faça um Programa que pergunte quanto você ganha por hora e o 
    número de horas trabalhadas no mês. Calcule e mostre o
    total do seu salário no referido mês.
'''

valor_hora = input('Qual o valor do salario por hora: R$')
horas_trabalhadas_mes = input('Quantas horas trabalhou no mês: ').replace(':', '.')
total_a_receber = float(valor_hora) * float(horas_trabalhadas_mes) 


print(f'O total a receber neste mês é: R${total_a_receber}')
