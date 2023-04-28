# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#       a - o produto do dobro do primeiro com metade do segundo .
#       b - a soma do triplo do primeiro com o terceiro.
#       c - o terceiro elevado ao cubo.

numero_int_1 = int(input('Informe um número inteiro: '))
numero_int_2 = int(input('Informe outro número inteiro: '))
numero_float = float(input('Informe um número real: '))


calculo_1 = (numero_int_1 * 2) * (numero_int_2 / 2)
calculo_2 = (numero_int_1 * 3) + numero_float
calculo_3 = numero_float ** 3

print(f'O produto do dobro de {numero_int_1} com metade de {numero_int_2} é {calculo_1}')
print(f'A soma do triplo de {numero_int_1} com {numero_float} é {calculo_2}')
print(f'O número {numero_float} elevado ao cubo é {calculo_3:.2f}')