'''
Faça um programa que leia um angulo qualquer e mpostre na terla o valor do seno, cosseno e tangente desse angulo
'''

from math import tan,cos,sin,radians

angulo = float(input('Digite o angulo: '))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O valor da tangente é {:.2f}\nOvalor do coseno é {:.2f}\nOvalor do seno é {:.2f}'.format(tangente,coseno,seno))