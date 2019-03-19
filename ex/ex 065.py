'''
Crei um programa que leie varios numeros inteiros pelo teclado
no final da execução mostre a media entre todos os valores digitados e qual foi o maior e menor valor
o programa deve perguntar se o usuario quer continuar
'''

continua = 'S'
maior = 0
menor = 0
soma = 0
count = 0

while continua == 'Ss':
    num = int(input('Digite um numero: '))

    if count == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

    soma += num
    count += 1
    continua = str(input('Para continuar digite "S"')).upper().strip()

print('\nForam digitado {} numeros\nA media entre eles foi {:.2f}\nO maior numero digitado foi {} e o menor {}'.format(count, soma / count, maior, menor))
