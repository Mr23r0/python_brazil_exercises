'''Faça um programa para a leitura de duas notas parciais de um aluno. 
    O programa deve calcular a média alcançada por aluno e apresentar:
        A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
        A mensagem "Reprovado", se a média for menor do que sete;
        A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
status = ''
if (media == 10):
    status = "APROVADO COM DISTINÇÃO"
elif (media >= 7 ):
    status = "APROVADO"
else:
    status = "REPROVADO"

print(f'A média do aluno é: {media:.2f}\n'\
      f'Status: {status}')

