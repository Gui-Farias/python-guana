'''
Um professor quer sortear um dos seus quatros alunos para apagar o quadro, faça um programa que ajude ele,
lendo o nome deles e eescrevendo o nome do escolhido
'''

from random import choice

alunos = ['Guilherme', 'Marcone', 'Sorbana', 'Pink Panther']
print('O aluno escolhido para limpar o quadro foi {}'.format(choice(alunos)))