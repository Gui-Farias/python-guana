'''
Faça um programa que leia o nome completo de uma pessoa, mostando em seguinda o primeiro e o ultimo nome
separadamente
'''

nome = input('Digite o seu nome completo: ').strip()
firstes = nome.find(' ')
lastes = (nome.rfind(' '))+1
print('O seu primeiro nome é: \n{}\n{:=^30}\nO seu ultimo nome é:\n{}'.format(nome[:firstes], '', nome[lastes:]))
