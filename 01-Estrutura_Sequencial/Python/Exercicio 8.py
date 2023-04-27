# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print('########## CALCULO DE SALÁRIO ##########')

ganho_hora = float(input('Quanto você ganha por hora trabalhada: '))
hora_trabalhada = float(input('Quantas horas você trabalhou? '))

resultado = ganho_hora * hora_trabalhada

print(f'Você trabalho {hora_trabalhada} hora(s) este mês e irá receber R$ {resultado:.2f}')

