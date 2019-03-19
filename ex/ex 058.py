'''
Melhore o jogo desafio 28 onde o computador vai pensar em um nuemro entre 0 e 10. só que agora o jogador
vai tentar até eçe acertar mostrando quando palpites foi necessario para acertar.
'''

from random import randint

print('xX'*36, '\nVou pensar em um numero de 0 a 10, vamos quanto tempo leva para acertar\n' + 'xX'*36)

num = randint(0, 10)
acerte = int(input('Digite um numero: '))
vez = 1

while acerte != num:
    acerte = int(input('ta dificil ai? kkk\nDigite um numero: '))
    vez += 1

if vez == 1:
    print('Ual voce acertou de primeira, tu é um cagão mesmo, eu escolhi o numero {}'.format(num))
elif vez > 7:
    print('KKKKK quase voce acerta de ultima em, você levou {} vezes para acertar o numero que eu pensei foi o {}'.format(vez, num))
else:
    print('Aee você acertou o numero que eu escolhi foi {}, você levou {} vezes para acertar'.format(num,vez))

