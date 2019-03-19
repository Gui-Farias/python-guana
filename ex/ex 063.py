'''
Escreva um programa que leia um numero n  interio qualquer e mostre na tela os numeros n primeiros
elementos de uma sequencia de fibonacci
ex:
0 > 1 > 1 > 2 > 3 > 5 > 8
'''


num = int(input('quantos termos deseja mostrar?  '))
seq1 = 0
seq2 = 1
cont = 3

print('{:=^50}'.format('Sequencia Fibonacci'))
print('{} > {} >'.format(seq1, seq2), end=' ')


while cont <= num:
    seq3 = seq1 + seq2
    print('{} >'.format(seq3), end=' ')
    seq1 = seq2
    seq2 = seq3
    cont += 1

print('FIM')
