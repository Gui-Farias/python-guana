'''
Crie um programa que leia o ano de nascimento de sete pessoas
nmo final mostre quantas pessoas é maior de idade considerando 21 anos
'''

from datetime import date

maior = 0
for x in range(1,8):
    idade = -(int(input('Digite o ano do seu nascimento: ')) - date.today().year)
    if idade > 21:
        maior += 1

print('{} pessoas sao maiores de idade.\ne {} são menores.'.format(maior, -(maior-7)))