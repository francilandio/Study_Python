# 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58.

print('########## CALCULO DE PESO IDEAL ##########')
print()

altura = float(input('Qual sua altura: '))

peso_ideal = (72.7 * altura) - 58

print(f'O peso ideal para alguém da sua altura é {peso_ideal}kg')

print()
print('########## FIM ##########')
