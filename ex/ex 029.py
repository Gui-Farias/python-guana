'''
Escreva um programa que leia a velocidade de um carro.
se ele utrapassar 80KM/hm mostre uma mensagem dizendo que ele foi multado.
a multa vai custar R$7,00 por cada KM acima do limeite
'''

velo = int(input('Digite a velocidade do carro em KM: '))

if velo > 80:
    print('Você foi multado por execeso de velocidade!')
    multa = (velo - 80) * 7
    print('O valor da multa é de R${:.2f}'.format(multa))
else:
    print('Parabens você é um motorista conciente!')

