# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
#   salário bruto.
#   quanto pagou ao IR.
#   quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#   o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   + Salário Bruto : R$
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#   = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

print('########## CALCULO SALÁRIO ##########')
print()

valor_hora = float(input('Quanto você ganha por hora trabalhada? '))
hora_trabalhada = float(input('Quantas horas você trabalhou? '))

salario_bruto = valor_hora * hora_trabalhada
ir = (salario_bruto) * (11/100) # 11%
inss = salario_bruto * (8/100) # 8%
sindicato = salario_bruto * (5/100) # 5%
salario_liquido = salario_bruto - ir - inss - sindicato

print()
print(f'Seu salário bruto foi de R$ {salario_bruto:.2f}')
print()
print(f'- IR (11%): R$ {ir:.2f}')
print(f'- INSS (8%): R$ {inss:.2f}')
print(f'- Sindicato (5%): R$ {sindicato:.2f}')
print()
print(f'Seu salário liquido é de R$ {salario_liquido:.2f}')

print()
print('########## FIM ##########')