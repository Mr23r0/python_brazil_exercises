n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')


if (n1.isalpha() == True or n2.isalpha() == True):
    print('Você não digitou um número')
else:
    soma = float(n1) + float(n2)
    print(f'A soma entre {n1} e {n2} é: {soma}')