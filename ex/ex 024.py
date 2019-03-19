'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome 'SANTO'.
'''

city = str(input('Digite o nome de uma cidade: ')).strip().capitalize()

print('a cidade "{}" começa com "Santo"?\n{}'.format(city, 'Santo' in city[:city.find(' ')]))
