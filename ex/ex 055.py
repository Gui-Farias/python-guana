'''
Faça um programq que leia o peso de cinco pessoas e no final mostre qual foi o maior e o menor peso lidos
'''


maior = 0
menor = 0
for x in range(1,6):
    peso = float(input('Digite o seu peso: '))

    if x == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O maior peso digitado foi {:.2f}Kg\nO menor peso foi {}Kg'.format(maior, menor))
