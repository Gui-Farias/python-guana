'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem de zero até vinte.
Seu programa devera ler um numero pelo teclao e mostrar por extenso
'''


# tunum = 'ZERO', 0, 'UM', 1, 'DOIS', 2, 'TRES', 3, 'QUATRO', 4, 'CINCO', 5, 'SEIS', 6, 'SETE', 7, 'OITO', 8, 'NOVE', 9, 'DEZ', 10, 'ONZE', 11, 'DOZE', 12, 'TREZE', 13, 'CATORZE', 14, 'QUINZE', 15, 'DESSEISEIS', 16, 'DESSESETE', 17, 'DESSEOITO', 18, 'DESSENOVE', 19, ' VINTE', 20
tunum = 'ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO',\
        'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE',\
        'DEZ', 'ONZE', 'DOZE', 'TREZE', 'CATORZE',\
        'QUINZE', 'DESSEISEIS', 'DESSESETE', 'DESSEOITO',\
        'DESSENOVE', ' VINTE'

while True:
    num = int(input('Digite um numero de 0 a 20: '))

    while 0 < num > 20:
        num = int(input('Numero invalido, digite um numero de 0 a 20: '))

    print(f'Voce digitou {tunum[num]}')

    cont = int(input('Caso desja continuar digite 1 '))
    if cont != 1:
        break
