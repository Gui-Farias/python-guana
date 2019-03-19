'''
004  Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivoe todas as
infomraçoes possiveis sobre ela
'''

texto = input('Digite algo: ')
print('Você digitou: {}'.format(texto))
print('{} é da class {} '.format(texto, type(texto)))
print('{} é um numero? {}' .format(texto, texto.isalnum()))
print('{} é alfabetico? {}'.format(texto, texto.isalpha()))
print('{} é um decimal? {}'.format(texto, texto.isdecimal()))
print('{} é numerico? {}'.format(texto, texto.isnumeric()))
print('{} é impresso? {}'.format(texto, texto.isprintable()))
print('{} é um espaço? {}'.format(texto, texto.isspace()))
print('{} está capitalizado? {}'.format(texto, texto.istitle()))
print('{} está tudo em maisculo? {}'.format(texto, texto.isupper()))
print('{} está tudo em minusculo? {}'.format(texto, texto.islower()))
