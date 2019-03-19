'''
Crie um programa que leia o nome e o preço de varios produtos
o programa devera perguntar se o usuario vai continuar, no final mostre
- Qual é o total gasto
- quantos produtos custam mais de 1000
- Qual é o nome do produto mais barato
'''

menor = maior = total = cont = 0
nomebarato = ''

while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o seu valor R$'))

    total += valor
    cont += 1

    if valor > 1000:
        maior += 1

    if menor == 0 or valor < menor:
        menor = valor
        nomebarato = produto

    continuar = str(input('Deseja continuar? ')).upper().strip()

    if continuar != 'S' and continuar != 'SIM':
        break

print(f'Ao todo foram passado {cont} produtos o valor total deu R${total:.2f}\nsendo que {maior} produtos custou mais de R$1000.00 e o {nomebarato} foi o produto mais barato com o valor de R${menor:.2f}')