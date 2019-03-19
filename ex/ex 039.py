'''
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
- se ele ainda vai se alistar
- se é a hora de se alistar
- se já passou da hora
mostrar quanto tempo falta ou quanto tempo ja passou
'''

from datetime import date

ano = int(input('{}Digite o ano do seu nascimento:{} '.format('\033[7m', '\033[m')))

idade = date.today().year - ano

if idade == 18:
    print('\033[0;32mSe lascou, tem que se alistar esse ano, ou vai ficar em divida com o pais!!\033[m')
elif idade > 18:
    print('\033[0;36mVoce se alistou faz {} anos{}'.format(idade-18, '\033[m'))
elif idade < 18:
    print('\033[35mCalma pequeno garfanhoto o seu dia de se alistar ainda vai chegar, falta {} anos{}'.format(-(idade-18), '\033[m'))
