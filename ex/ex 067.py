'''
Faça um programa que mostre a tabuada de varios numeros um de cada vez
o programa sera interrrompido quando o numero for nagativo
'''

while True:
    num = int(input('Digite o  numero para fazer a tabuado: '))
    if num < 0:
        print('Não é possivel fazer tabuada de numero negativo')
        break

    for x in range(1, 11):
        print(f'{num} x {x} = {num * x}')
