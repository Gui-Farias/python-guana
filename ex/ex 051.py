'''
Desenvolva um programa que leia o primeiro termo e a razao de uma PA. no final mostre os 10 primeiros termos
dessa prgressão
'''

i = int(input('Digite em que numero deseja começar: '))
pa = int(input('Digite o valor que deseja de salto: '))
print('Os 10 primeiros numeros dessa progressão foram: ')

for x in range(i, (i+9*pa)+pa, pa):
     print(x, end=' ► ')
print('Acabou')
