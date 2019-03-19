

print('\033[0;30;41mteste\033[m')
print('\033[4;33;44mteste\033[m')
print('\033[1;35;43mteste\033[m')
print('\033[30;42mteste\033[m')
print('\033[mteste\033[m')
print('\033[7;30mteste\033[m')


cores = {
    'limpa': '\033[m',
    'azul': '\33[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;30m'
}

nome = 'Guilherme'
print('Olá muito prazer em te conhecer, {}{}{}!!!'.format('\033[1;35m', nome, '\033[m'))
print('Olá muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))

