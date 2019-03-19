'''
Crie um programa que faça o computador jogar jokenpô com você;
'''

from random import choice
from time import sleep

opcao = ['PEDRA', 'PAPEL', 'TESOURA']
bot = 0
jogador = 0
empate = 0

nome = str(input('\nOlá, por favor informe o seu nome: ')).upper()
print('E ai {} você acha que é capaz de vencer o BOT TREVOSO? kkkkkk'.format(nome))
print('Que os jogos começem, para finalizar digite 4')
print('-='*30, '\nSEJAAAAA BEM VINDOOO AO JOOOKENNNPOOOOOO\nLista das escolhas:\n[1] - Pedra\n[2] - Tesoura\n[3] - Papel')

while True:
    print('-='*30,'\nPLACAR DO JOOOOOKEENNNNNPOOOOO:\nBOT: {} -=- {}: {} -=- EMPATE: {}\n'.format(bot, nome, jogador, empate) + '-='*30, '\n')
    escolhajoga = str(input('FAÇA SUA ESCOLHA:')).strip()
    escolhabot = choice(opcao)

    if escolhajoga != '1' and escolhajoga != '2' and escolhajoga != '3':
        print('aaa que pena que acabou, vamos conferir o resultado...\n')
        sleep(3)
        break

    print('JOOOOOOO')
    sleep(0.5)
    print('KENNNN')
    sleep(0.5)
    print('POOOOOOOOOOOOOOOO\n')
    sleep(0.5)

    if escolhajoga == '1':
        if escolhabot == 'PEDRA':
            print('IIII Deu empate, eu tambem escolhi {}'.format(escolhabot))
            empate = empate +1
        elif escolhabot == 'PAPEL':
            print('HAHA, Você perdeu, eu joguei {}!'.format(escolhabot))
            bot = bot +1
        elif escolhabot == 'TESOURA':
            print('Droga você me venceu desssa vez, eu escolhi {}'.format(escolhabot))
            jogador = jogador+1
    elif escolhajoga == '3':
        if escolhabot == 'PAPEL':
            print('IIII Deu empate, eu tambem escolhi {}'.format(escolhabot))
            empate = empate +1
        elif escolhabot == 'TESOURA':
            print('HAHA, Você perdeu, eu joguei {}!'.format(escolhabot))
            bot = bot +1
        elif escolhabot == 'PEDRA':
            print('Droga você me venceu desssa vez, eu escolhi {}'.format(escolhabot))
            jogador = jogador +1
    elif escolhajoga == '2':
        if escolhabot == 'TESOURA':
            print('IIII Deu empate, eu tambem escolhi {}'.format(escolhabot))
            empate = empate +1
        elif escolhabot == 'PEDRA':
            print('HAHA, Você perdeu, eu joguei {}!'.format(escolhabot))
            bot = bot +1
        elif escolhabot == 'PAPEL':
            print('Droga você me venceu desssa vez, eu escolhi {}'.format(escolhabot))
            jogador = jogador +1

print('-='*10,'Jogo Finalizado', '-='*10)
print('PLACAR FINAL:\nBOT: {} -=- {}: {} -=- EMPATE: {}'.format(bot, nome, jogador, empate))
if jogador > bot:
    print('Parabens! {} Você conseguiu vencer o bot e com uma vantagem de {} pontos'.format(nome, jogador-bot))
elif jogador < bot:
    print('HAHA, Fracassado eu sabia que você não ia me vencer, o BOT TREVOSO ganhou com uma vantagem de {} pontos'.format(bot-jogador))
else:
    print('Esse foi dificil deu empate {}'.format(empate))
