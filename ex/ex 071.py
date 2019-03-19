'''
Crie um programa que simule o funcionamento de um caixa eletronico
no inicio pergunte qual sera o valor a ser sacado
o programa vai informar quantas cedulas de cada valor serao entregues

obs considere nostas de 50 20 10 e 1
'''

c50 = c20 = c10 = c1 = 0
saque = int(input('Quanto deseja sacar? '))
while saque != 0:
    if saque >= 50:
        saque -= 50
        c50 += 1
    elif saque >= 20:
        saque -= 20
        c20 += 1
    elif saque >= 10:
        saque -= 10
        c10 += 1
    elif saque < 10:
        saque -= 1
        c1 += 1
    else:
        print('\033[31mNumeros nagativo nao sao valido!')
print(f'Voce vai receber:\n{c50} notas de R$50,00\n{c20} notas de R$20,00\n{c10} notas de R$10,00\n{c1} notas de R$1,00')
