'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
'''

import datetime


ano = int(input('Digite o ano que deseja saber se é bissexto coloque 0 para o ano atual: '))

if ano == 0:
    ano = datetime.date.today().year  #pega o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} NÃO é bissexto'.format(ano))
