'''
012 Faça um algorito que lia o preço de um produto e mostre sua novo preço com 5% de desconto
'''

produnome = input('Que produto deseja ver com o desconto? ')
produ = float(input('Qual é o valor altual do {}?'.format(produnome)))

producomdesc = produ - (produ*0.05)
print('o {} com o desconto de 5% fica por {:.2f}'.format(produnome,producomdesc))

