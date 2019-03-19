'''
Crie um programa que leia uma frase qualquer e diga se ela é palindromo desconsiderando os espaços
palindromo é uma frase que se ler dos dois lados que da o mesmo
ex:
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
'''


frase = str(input('Digite uma frase: ')).upper().strip().split()
frasejunta = ''.join(frase)
frasecontra = ''
frasecontra2 = frasejunta[::-1]

for x in range(len(frasejunta) - 1, -1, -1):
    frasecontra += frasejunta[x]

if frasecontra == frasejunta:
    print('{}A frase {} é PALINDORMO!'.format('\033[0;33m', ' '.join(frase)))
else:
    print('{}A frase {} não é PALINDORMO'.format('\033[0;31m', ' '.join(frase)))

if frasejunta == frasecontra2:
    print('é palindormo {}'.format(frasecontra2))
else:
    print('Não é palindormo {}'.format(frasecontra2))
