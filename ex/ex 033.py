'''
Faça um program que leia tres numeros e mostre qual é o maior e qual é o menor
'''

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

if num1 > num2 and num1 > num3:
    print('O maior numero é o {}'.format(num1))
    if num2 > num3:
        print('O menor numero é o {}'.format(num3))
    else:
        print('O menor numero é o {}'.format(num2))
elif num2 > num3 and num2 > num1:
    print('O maior numero é o {}'.format(num2))
    if num3 > num1:
        print('O menor numero é o {}'.format(num1))
    else:
        print('O menor numero é o {}'.format(num3))
else:
    print('O maior numero é o {}'.format(num3))
    if num1 > num2:
        print('O menor numer é o {}'.format(num2))
    else:
        print('O menor numero é o {}'.format(num1))
