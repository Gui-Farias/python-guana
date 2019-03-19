'''
Crie um programa que tenha uma tupla com varias palavras
depois voce deve mostrar para cada palavra quais sao suas vogais
'''

pala = 'pudim', 'arroz', 'batata', 'livro', 'jogo', \
       'video', 'game', 'chocolate', 'pastel', 'tapioca'

for x in pala:
    print(f'\nNa palavra {x} tem as vogais: ', end=' ')
    for l in range(0,len(x)):
        if x[l] in 'aeiou':
            print(x[l], end=' ')

        '''
        if x[l] == 'a':
            print('a', end=' ')
        elif x[l] == 'e':
            print('e', end=' ')
        elif x[l] == 'i':
            print('i', end=' ')
        elif x[l] == 'o':
            print('o', end=' ')
        elif x[l] == 'u':
            print('u', end=' ')
        '''
        
print('\n\n')

for x in pala:
    print(f'\nNa palavra {x} temos ', end=' ')
    for l in x:
        if l in 'aeiou':
            print(l, end=' ')
