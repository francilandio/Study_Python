# 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#       Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
#       João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#       Gravar na variável <excesso> a quantidade de quilos além do limite e na variável <multa> o valor da multa que João deverá pagar. 
#       Imprima os dados do programa com as mensagens adequadas.

print('########## CALCULO DE PESO IDEAL POR SEXO ##########')
print()

peso = float(input('Qual o peso dos peixes? '))
multa = float(4)

if peso > 50:
    excesso = peso - 50
    multa_pagar = excesso * multa
    print(f'O peso dos peixes excedeu {excesso} kg, você deverá pagar R${multa_pagar:.2f} pelo excesso.')
else:
    print(f'O peso está dentro do limite permitido!')

print()
print('########## FIM ##########')