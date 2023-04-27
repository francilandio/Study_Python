# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print('########## CONVERSOR CELSIUS PARA FAHRENHEIT ##########')
print()

celsius = float(input('Informe a temperatura em Celsius que deseja converter: '))

fahrenheit = (celsius * 1.8) + 32

print(f'{celsius:.2f} °C equivalem a {fahrenheit:.2f} °F.')
print()
print('########## FIM ##########')