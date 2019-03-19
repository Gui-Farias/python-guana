'''
Escreva uum programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela nao pode execer 30% do salario
ou entao o emprestimo será negado.
'''

from time import  sleep

print('-='*30)
nome = str(input('\033[0;32mBom dia Sr/Sra, qual o seu nome? '))
casa = float(input('\033[0;32mSejá bem vindo {}, qual seria o valor da casa que desja comprar?\nR$'.format(nome)))
anos = int(input('\033[0;32mEm quantos anos deseja parcelar essa casa? '))
salario = float(input('\033[0;32mPor favor por favor informar tambem o seu salario.\nR$'))
print('\033[1;35mPROCESSANDO...')
sleep(3)

parcela = casa / (anos *12)

print('Para pagar essa casa de R${:.2f} em {} anos a prestção sera de R${:.2f} por mês'.format(casa, anos, parcela))
if parcela > ((salario /100) *30):
    print('\033[0;31mDesculpas {}, mas o valor das parcelas ficaria muito alto, não podemos realizar esse financiamento'.format(nome))
else:
    print('\033[0;34m{}, o seu emprestimo para a casa foi concedido!!'.format(nome))

