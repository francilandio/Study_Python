# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print('########## TEMPO DE DOWNLOAD ##########')
print()

tamanho_arquivo = int(input('Qual o tamanho do arquivo? '))
velocidade = int(input('Qual a velocidade da sua internet? '))

tempo = (tamanho_arquivo / (velocidade / 8)) / 60

print(f'Para realizar o download de um arquivo de {tamanho_arquivo} MB, a uma velocidade de {velocidade} Mbps levará {tempo:.0f} minuto(s).')

print()
print('########## TEMPO DE DOWNLOAD ##########')