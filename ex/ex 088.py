'''
Faça um programa que ajude um jogador da mega sena a criar palpites
o programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros ente 1 e 60
para cada jogo castrado tudo em uma lista composta
'''

from  random import randint
from  time import sleep


vez = int(input('Quantas vezes deseja jogar? '))
jogo = []
for z in range(0, vez):
    jogovez = []
    for x in range(0,6):
        temp = randint(1,60)
        if temp not in jogovez:
            jogovez.append(temp)
        else:
            while temp in jogovez:
                temp = randint(1,60)
            jogovez.append(temp)
    jogo.append(jogovez[:])
    vez -= 1
print(f'Os jogos sorteador foram: ')

for x in jogo:
    print(sorted(x))
    sleep(1)
