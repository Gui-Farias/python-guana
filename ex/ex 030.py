'''
Crie um programa que leie um numero inteiro e mostre na tela se ele pe par ou impar
'''

num = int(input('Digite um numero inteiro e veja se é par ou impar: '))

if num == 0:
    print('O numero digitado foi zero e zero é nulo')
elif num % 2 == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é IMPAR'.format(num))
