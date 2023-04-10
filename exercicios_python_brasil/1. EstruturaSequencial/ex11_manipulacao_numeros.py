''' Faça um Programa que peça 2 números inteiros e um número decimal. Calcule e mostre:
        a. o produto do dobro do primeiro com metade do segundo .
        b. a soma do triplo do primeiro com o terceiro.
        c. o terceiro elevado ao cubo.'''

n1 = input('Digite um número inteiro: ')
n2 = input('Digite outro número inteiro: ')
n_decimal = input('Digite um numero decimal: ')
a = (int(n1)*2) * (int(n2)/2)
b = (int(n1)*3) + (float(n_decimal)) 
c = float(n_decimal)**3
print('=-'*25)
print(f'O produto do dobro de {n1} com metade de {n2} é: {a}\n'\
      f'A soma do triplo de {n1} com {n_decimal} é : {b}.\n'\
      f'O numero {n_decimal} elevado ao cubo é: {c}\n')
