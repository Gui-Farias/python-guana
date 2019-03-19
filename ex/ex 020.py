'''
O mesmo professor quer sortear a ordem de aporesentação de trabalhos dos akunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
'''

from random import shuffle

aluno = ['Guilherme', 'Marcone', 'Sorbana', 'Pink Panther']
shuffle(aluno)
print('A ordem dos alunos a apresentar o trabalho é: \n{}'.format(aluno))
