'''
Refaça o Desafio 009, mostrando a tabuada de um numero que o usuario esolher so que agora com o laço for
'''

num = int(input('Digite o numero que deseja fazer a tabuada: '))
numat = int(input('Digite até que numero deseja ter a tabuada: '))
temp = 0

for x in range(0, numat+1):
    print('{} x {} = {}'.format(num, temp, num*temp))
    temp += 1
