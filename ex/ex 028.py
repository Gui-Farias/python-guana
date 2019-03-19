'''
Escreva um programa que faça o computador "Pensar" em um numero inteiro entre 0 e 5 e peça para o usuario
tentar descobrir qual foi o numero escolihdo pelo computador.
o porgrama devera escrever na tela se o usuario venceu ou perdeu
'''

from random import randint  # importa o modo de randomiza um numero
from time import sleep  # importa um mode de espera

num = randint(0, 5)  # sorteia um numero entre 0 e 5

print('-=' * 20)
print('Vou pensar em um numero, você consegue adivinhar?')
print('-=' * 20)
acerte = int(input('Digite um numeor de 0 a 5 e tente vencer a maquina: '))

print('Processando...')
sleep(2)  # colocar o tempo para espera

if acerte == num:
    print('Parabens voce acertou!!')
elif acerte != num:
    print('Não foi dessa vez, mas continue tentando ')

