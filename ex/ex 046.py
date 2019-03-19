'''
Faça um programa que mostre na tela uma contagem regrasiva para o estouro de fgos de artificio
ido de 10 até 0 com pausa de 1 segundo entre eles.
'''

from time import sleep
import emoji

print('xX'*10,' Contagem regrssiva ', 'xX'*10)


for x in range(10, -1, -1):
    print(x)
    sleep(1)

print(emoji.emojize('\033[31mBOOMMMMMMMMMMM :boom: :boom: :boom:', use_aliases=True))
