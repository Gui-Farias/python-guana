'''
Desenvolva um program que pergunte a distancia de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para  viagens até 200KM e R$0.45 para viagens mais longas
'''

dist = float(input('Digite a distancia da vigaem que vai fazer: '))

if dist > 200:
    print('O valor da  viagem vai ser R${:.2f}'.format(dist * 0.45))
else:
    print('O valor da viagem vai ser R${:.2f}'.format(dist * 0.50))
