'''
Desenvolva uma logica que leia o peso e a lautra de uma pessoa e calcule o seu IMC e mostre seu status:
- abaixo de 18.5: Abaixo do peso
- entre 18.5 e 25: peso ideal
- entre 25 e 30: Sobrepeso
- de 30 a 40: obesidade
- acima de 40: obesidade morbida
'''

from time import  sleep

print('\033[0;36m^-'*29,'\nCalculadora do IMC', '\n', '^-'*29)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso /(altura*altura)
cate = ''

if imc <= 18.5:
    cate = '\033[33mABAIXO DO PESO!\033[m'
elif imc > 18.5 and imc <= 25:
    cate = '\033[35mPESO IDEAL!\033[m'
elif imc > 25 and imc <= 30:
    cate = '\033[34mSOBREPESO!\033[m'
elif imc > 30 and imc <= 40:
    cate = '\033[32mOBESIDADE!\033[m'
else:
    cate = '\033[31mOBESIDADE MORBIDA!\033[m'

print('Estamos calculando o seu Indice de massa corporal...')
sleep(3)
print('\nO seu IMC é {:.2f} ele esta categorizado como {}'.format(imc, cate))
