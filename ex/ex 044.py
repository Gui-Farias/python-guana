'''
Elabore um programa que calcule o valor a ser pago por um porduto considerando o seu preço normal e forma de pag
- avista dinheiro/cheque: 10% de desconto
- a vista no cartão: 5 % de desconto
- em até 2x no cartão: preço normal
- mais de 3x no cartão: 20% de juros
'''

print('\033[36m-='*30, '\nRevendedor IVONE\n' + '-='*30, '\033[m')

valor = float(input('Qual foi o valor total da sua compra ?\n'))
pag = int(input('Digite qual vai ser a forma de pagamento, trabalhamos com:\n1-Dinheiro\n2-Cheque\n3-Cartão\nDigite o numero referente a forma de pagamento:\n'))


if pag != 1 and pag != 2 and pag != 3:
    print('\033[31mVocê digitou uma opção invalida!!\033[m')
if pag == 3:
    parcela = int(input('Digite a quantidade de parcelas: '))

if pag == 1 or pag == 2:
    print('\nEssa opção tem 10% de desconto\nO Valor final a ser pago ficou por {:.2f}'.format(valor/100*90))
elif pag == 3 and parcela == 1:
    print('\nEssa opção tem 5% de desconto\nO valor final a ser pago ficou por {:.2f}'.format(valor/100*95))
elif pag == 3 and parcela == 2:
    print('\nEssa opção não tem descostos\nO Valor a ser pago é {:.2f}'.format(valor))
elif pag == 3:
    print('\nEssa opção tem um juros de 20%\nO Valor final ser pago é de {:.2f}'.format(valor/100*120))
