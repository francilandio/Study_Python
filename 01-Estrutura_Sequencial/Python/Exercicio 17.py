# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

print('########## LOJA DE TINTAS 2 ##########')
print()

area = int(input('Quantos m² deseja pintar? '))

litros = (area / 6) * 1.1
latas = math.ceil(litros / 18)
valor_lata = latas * 80
galao = math.ceil(litros / 3.6)
valor_galao = galao * 25

mixlatas = round(litros / 18)
mixgaloes = round(litros - mixlatas * 18) / 3.6

if (litros - (mixlatas * 18) % 3.6 != 0):
    mixgaloes += 1
    total_mix = (mixlatas * 80) + (mixgaloes * 25)

print(f'Se for comprar só latas de 18 litros irá precisar de {latas} latas e irá custa R$ {valor_lata:.2f}')
print(f'Se for comprar só galões de 3,6 litros irá precisar de {galao} galão(ões) e irá custar R$ {valor_galao:.2f}')
print(f'Se deseja mesclar latas e galões para dar o que precisar, realmente será necessário {mixlatas} lata(s) e {mixgaloes} galão(ões) e irá custar R$ {total_mix:.2f}')

print()
print('########## FIM ##########')