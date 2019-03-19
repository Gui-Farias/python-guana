'''
Escreva um programa que leia dois numeros interios e compare os. mostrando na tela:
o maior
o menor
e se forem igual
'''

num1 = int(input('{}Digite um numero interio: {}'.format('\033[0;33m', '\033[m')))
num2 = int(input('{}Digite um segundo numero: {}'.format('\033[0;33m', '\033[m')))

if num1 == num2:
    print('\033[1;34mOs valores digitados foram os mesmo')
elif num1 > num2:
    print('O maior valor foi o \033[1;35m{}\033[m e o menor valor foi \033[1;31m{}\033[m'.format(num1, num2))
else:
    print('O maior valor foi o \033[1;35m{}\033[m e o menor foi o \033[1;31m{}\033[m'.format(num2, num1))
