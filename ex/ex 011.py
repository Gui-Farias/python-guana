'''
011 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta
necessario para pinta-la, sabendo que cada litro de tinta pinta uma area de 2M².
'''

largura = float(input('Qual a largura em metros da parede que deseja pintar? '))
altura = float(input('Qual a altura em metros da parede que deseja pintar?'))

area = largura * altura
areatinta = area / 2

print('Voce deseja pintar uma area de {} metros para isso sera necessario {} litros de tinta'.format(area,areatinta))

