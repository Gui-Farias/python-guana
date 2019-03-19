'''
Crie um programa que tenha uma tupla unica com os nomes de produtos e seus preços
-mostrar uma lsitagem com os produtos e preços
'''

prod = 'arroz', 2.50, \
       'pacoca', 0.50, \
       'xampu', 7.67, \
       'livro', 10.99, \
       'batata', 7.45

print(f'{" Preços da lojinha ":-^40}')

for x in range(0, len(prod)):
    if x % 2 == 0:
        print(f'{prod[x]:.<30}', end=' ')
    else:
        print(f'R$ {prod[x]:>7.2f}')

print('-'*40)