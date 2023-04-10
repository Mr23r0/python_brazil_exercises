'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = input('Digite apenas uma letra: ')
if (letra.isalpha()):
    if (len(letra) > 1):
        print('Você digitou mais de uma letra.')
    elif ('a' in letra or 'e' in letra or 'i' in letra or 'o' in letra or 'u' in letra):
        print('A letra digitada é uma vogal.')
    else:
        print('A letra digitada é uma consoante.')
else:
    print('Você não digitou uma letra.')
