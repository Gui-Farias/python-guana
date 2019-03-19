'''
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares
se for impar desconsiderar
'''

par = 0

for x in range(1, 7):
    num = int(input('Digite o {} valor:\n'.format(x)))
    if num % 2 == 0:
        par += num
print('A soma dos valores pares digitados foi: {}'.format(par))
