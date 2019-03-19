'''
Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
- mostrar os numeros gerado
- o menor valor
- o maior valor
'''

from random import randint

num = randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)

print(f'Os valores sorteado foram: ', end='')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior valor foi {max(num)}\nO menor valor foi {min(num)}')

