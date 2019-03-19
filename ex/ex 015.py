'''
Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
os quais ele for alugado. Calcule o preço a pagar, sbaendo que o carro custa R$60.00 por dia e R$0.15 por km rodado
'''

km = float(input('Qual foi a distancia percorrida em km? '))
dia = int(input('Por quantos dias ficou com o carro? '))

totalkm = km * 0.15
totaldia = dia * 60

total = totalkm + totaldia

print('O total das diarias ficou  no vlaor de R${:.2f}'.format(total))
