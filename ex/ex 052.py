'''
Faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo
'''



num = int(input('Digite um valor: '))

if num / num == 1 and num % 2 != 0 and num % 3 != 0:
    print('\033[0;36mo numero {} é primo!'.format(num))
else:
    print('\033[0;31mO numero {} não é primo'.format(num))


temp = 0

for x in range(1, num + 1):
    if num % x == 0:
        print('\033[0;36m', end='')
        temp += 1
    else:
        print('\033[0;31m', end='')
    print(x, end=' ')

if temp == 2:
    print('\n{}O numero {} foi dividido por {} vezes sendo assim ele É primo!'.format('\033[0;36m', num, temp))
else:
    print('\n{}O numero {} foi dividido por {} vezes sendo assim ele NÃO é primo!'.format('\033[0;31m', num, temp))
