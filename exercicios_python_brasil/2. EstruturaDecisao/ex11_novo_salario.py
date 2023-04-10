'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
    salário atual:
        salários até R$ 280,00 (incluindo) : aumento de 20%
        salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
'''
salario = float(input('Informe o salario do colaborador: R$'))
novo_salario = float(0)
percentual = 0
valor_do_aumento = 0

if salario > 1500.00:
    percentual = 0.05
    valor_do_aumento = salario * percentual
    novo_salario = salario + valor_do_aumento

elif salario > 700.00:
    percentual = 0.10
    valor_do_aumento = salario * percentual
    novo_salario = salario + valor_do_aumento

elif salario > 280.00:
    percentual = 0.15
    valor_do_aumento = salario * percentual
    novo_salario = salario + valor_do_aumento
else:
    percentual = 0.20
    valor_do_aumento = salario * percentual
    novo_salario = salario + valor_do_aumento

print(f'Sálario antigo: R${salario:.2f}\n'\
      f'Percentual aplicado: {percentual*100:.0f}%\n'\
      f'Aumento de: R${valor_do_aumento:.2f}\n'\
      f'Novo sálario: R${novo_salario:.2f}\n'\
    )