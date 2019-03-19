'''
Crie um programa que leia um  numero Real qualquer pelo teclado e mostre na tela sua porção interira
ex:
Digite um numero: 6.127
o numero 6.127 tem a parte interia 6
'''

from math import floor, trunc

num = float(input('Digite um numero Real: '))
print('O numero {} tem a perte {} como interia.'.format(num, trunc(num)))
print('O numero {} tem a parte {} como inteira.'.format(num, floor(num)))
print('O numero {} tem a parte {:.0f} como interia.'.format(num, num))
print('O numero {} tem a parte {} como interia.'.format(num, int(num)))
