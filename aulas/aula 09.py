
frase = 'Curso em video Python'

print(frase)
print(frase[3])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(frase[::2])

print('a frase {} tem {} caracter'.format(frase, len(frase)))

print('a frase {} tem {} "o" '.format(frase, frase.count('o')))
print('a frase {} tem {} "o" '.format(frase, frase.count('o', 0, 13)))
print(frase.find('deo'))  # mostra o indice que começa a frase
print(frase.find('Android'))  # mostra -1 pois nao foi encontrado
print('Curso' in frase)

print('a frase original é {}, a nova frase é {}'.format(frase, frase.replace('Python', 'Android')))

print(frase.upper())
print(frase.lower())
print(frase.capitalize())  # Deixa a primeira letra da frase em upper
print(frase.title())  # deixa a primeira letra de cada palavra em upper


novafrase = '   Aprenda Python  '

print(novafrase)
print(novafrase.strip())  # tira os espaços antes e depois da palavra
print(novafrase.rstrip())  # remove os espaços da direita
print(novafrase.lstrip())  # remove os espaços da esquerda



print(frase.split())  # gera uma lista com as palavras da frase

listafrase = frase.split()
print(listafrase)

print('-'.join(listafrase))  # tranforma uma lista em uma str
print(' '.join(listafrase))

