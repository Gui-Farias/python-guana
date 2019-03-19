'''
Crie um programa que leie varios numeros inteiros pelo teclado
o programa vai parar quando o usuario digitar 999
no final mostre quantos numeros foram digitados e qual foi a soma entre eles
'''

num = 0
soma = 0
cont = 1

while num != 999:
    num = int(input('Digite um numero: '))

    if num != 999:
        soma += num
        cont += 1

print('Você digitou {} numeros e a soma entre eles foi {}'.format(cont - 1, soma))
