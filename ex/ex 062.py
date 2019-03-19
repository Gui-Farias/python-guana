'''
Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos.
o programa encerrra quadno ele disser que quer mostrar 0 termos
'''

i = int(input('Digite em que numero deseja começar a PA: '))
s = int(input('Digite o valor que deseja de salto: '))
t1 = 1
t2 = 0

print('Os 10 primeiros numeros dessa PA foram:\n{}'.format(i), end=' ')

while t1 != 10:
    while t1 != 10:
        i += s
        print(i, end=' ')
        t1 += 1
    t2 = int(input('\nDeseja continuar com essa PA, se sim quer mais quantos numeros? '))
    if t2 == 0:
        t2 = 10
    else:
        t1 -= t2
