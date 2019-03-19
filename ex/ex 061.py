'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma pa, mostrando os 10 primeiros termos
da pa usando a estrutura while
'''

i = int(input('Digite em que numero deseja começar a PA: '))
s = int(input('Digite o valor que deseja de salto: '))
t = 1
print('Os 10 primeiros numero dessa PA foram :\n{}'.format(i), end=' ')

while t != 10:
    i += s
    print(i, end=' ')
    t += 1
