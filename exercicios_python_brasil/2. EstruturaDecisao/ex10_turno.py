'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = input('Qual turno você estuda? [M]atutino, [V]espertino ou [N]oturno: ').capitalize()

if turno.startswith('M'):
    print('Bom Dia!')
elif turno.startswith('V') or turno.startswith('Tar'):
    print('Boa Tarde!')
elif turno.startswith('N'):
    print('Boa Noite!')
else:
    print('Valor Inválido')