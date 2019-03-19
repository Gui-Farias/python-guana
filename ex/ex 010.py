'''
010 Crie um programa que leia quanto dinheiro uma pessoa tem na carteia e mostre quantos dolates ela pode comprar
considerar  US1,00 = R$ 3.27
'''

money = float(input('Digite quanto você tem na carteira: '))
dolar = money / 3.27
print('com {} reais é possivel comprar {:.2f} doletas'.format(money, dolar))

