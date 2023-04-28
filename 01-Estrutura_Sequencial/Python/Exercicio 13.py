# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#       a - Para homens: (72.7*h) - 58
#       b - Para mulheres: (62.1*h) - 44.7

print('########## CALCULO DE PESO IDEAL POR SEXO ##########')
print()

sexo = input('De qual sexo deseja saber o peso ideal? h/m: ')

if sexo == 'h':
    altura_homem = float(input('Qual a altura? '))
    resultado = (72.7 * altura_homem) - 58
    print(f'O seu peso ideal {resultado:.3f} kg')
else:
    altura_mulher = float(input('Qual a altura? '))
    resultado = (62.1 * altura_mulher) - 44.7
    print(f'O seu peso ideal {resultado:.3f} kg')

print()
print('########## FIM ##########')