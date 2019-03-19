'''
Crie um programa que calcule a soma entre todos os numeros impares qwue são multiplos de tres
e estão no intervalo de 1 até 500.
'''

soma = 0

for x in range(1,501):
    if x % 2 != 0 and x % 3 == 0:
        soma += x

print('A soma dos valores impares e multiplos de tres de 1 a 500 é {}'.format(soma))