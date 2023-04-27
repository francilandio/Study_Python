# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

print('########## CONVERSOR FAHRENHEIT PARA CELSIUS ##########')
print()
graus_f = float(input('Informe a temperatura: '))

graus_c = 5 * ((graus_f-32) / 9)

print(f'O valor de {graus_f:.2f} °F equivalem a {graus_c:.2f} °C.')
print()
print('########## FIM ##########')