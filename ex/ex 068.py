'''
Faça um programa que jogue par ou impar com o computador
o jogo so sera interrompido quando o jogador perder
mostrando o total de vitorias consecutivas que ele obteve
'''

from random import randint
cont = 0
while True:
    botnum = randint(1, 10)
    joga = str(input('Voce quer IMPAR ou PAR?' )).upper().strip()
    joganum = int(input('Digite um valor de 1 a 10: '))

    if joga != 'IMPAR' and joga != 'PAR':
        print('\033[31mVoce escolheu um valor difernte de PAR ou IMPAR!\033[m')
    elif 0 < joganum > 10:
        print('\033[31mVo digitou um numero invalido\033[m')
    elif joga == 'IMPAR':
        if (joganum + botnum) % 2 == 0:
            print(f'Há Há voce perdeu eu joguei {botnum}')
            break
        else:
            print(f'Boaa eu joguei {botnum}, vamos ser se consegue me vencer de novo\n')
            cont +=1
    elif joga == 'PAR':
        if (joganum + botnum) % 2 == 0:
            print(f'Boaa eu joguei {botnum}, vamos ver se consegue me vencer de novo\n')
            cont += 1
        else:
            print(f'Há Há voce perdeu eu joguei {botnum}')
            break
print(f'Voce obteve {cont} vitorias consegutivas')
