'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria de acordo com a idade:
- até 9 anos: mirim
- até 14 anos: Infantil
- até 19 anos: Junior
- até 20 anos: Senior
- acima : Master
'''

from datetime import date

idade = -(int(input('Bom dia, por favor informe sua data de nascimento: '))- date.today().year)

cate = '\033[32;40mMIRIM\033[m'

if idade <= 9:
    cate = cate
elif idade > 9 and idade <= 14:
    cate = '\033[33;40mINFANTIL\033[m'
elif idade > 14 and idade <= 19:
    cate = '\033[34;40mJUNIOR\033[m'
elif idade == 20:
    cate = '\033[35;40mSENIOR\033[m'
else:
    cate = '\033[36;40mMASTER\033[m'

print('{}Você está na categoria {}'.format('\033[7;30m', cate))
