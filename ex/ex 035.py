'''
Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se ela podem ou nao formar um
triangulo
'''
print('-='*20, '\nAnalizador de triangulos\n', '-='*20)
reta1 = float(input('Digite o primeiro segmento: '))
reta2 = float(input('Digite o segundo segmento: '))
reta3 = float(input('Digite o terceiro segmento: '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('É possivel formar um triangulo')
else:
    print('Não é possivel formar segmentos com as retas digitas')
