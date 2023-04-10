'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê: 
    a. salário bruto.
    b. quanto pagou ao INSS.
    c. quanto pagou ao sindicato.
    d. o salário líquido.
    e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
    Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
salario_hora = input('Qual o valor do salário por hora: ')
horas_trabalhadas = input('Quantas horas trabalhou este mês: ')
salario_bruto = float(salario_hora) * float(horas_trabalhadas)
ir_descontado = float(salario_bruto) * 0.11
inss_descontado = float(salario_bruto) * 0.08
sindicato_descontado = float(salario_bruto) * 0.05
descontos = ir_descontado + inss_descontado + sindicato_descontado
salario_liquido = salario_bruto - descontos


print('=-'*25)
print(f'Seu salário bruto mensal é: R${salario_bruto:.2f}\n'\
      '\n'
      'Foram descontados:\n'\
      f'R${ir_descontado:.2f} de imposto de renda\n'\
      f'R${inss_descontado:.2f} de INSS\n'\
      f'R${sindicato_descontado:.2f} de Sindicato\n'\
      f'Somando um total de R${descontos:.2f} em descontos\n'\
      '\n'
      f'Portanto seu salário líquido é R${salario_liquido:.2f}'
      )