'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras em maisculas
- O nome com todas miniculas
- Quantas letras ao todo (sem contar espaços)
- Quantas letrar tem o primeiro nome
'''

nome = input('Digite seu nome completo: ').strip()

print('Seu nome em maiscule é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))


espaco = nome.count(' ')
lees = len(nome) - espaco

print('Seu nome ao todo tem {} letras "Contando os espaços"'.format(len(nome)))
print('Seu nome sem os espaços tem {} letras'.format(lees))
print('Seu primeir noomte tem {} letras'.format(len(nome)-nome.count(' ')))

prinome = nome[:nome.find(' ')]

print('O seu primeiro nome é {} e ela tem {} letras'.format(prinome, len(prinome)))
