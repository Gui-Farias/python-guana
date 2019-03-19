'''
009 Faça um programa que leia um numero interiro qualquer e mostre na tela sua tabuada
'''

num = int(input('Digite o numero que deseja fazer a tabuada: '))
numt = int(input('Digite até que numero deseja ter a tabuada: '))
temp = 0
while temp <= numt:
    print('{} x {:2} = {}'.format(num,temp,num*temp))
    temp = temp + 1

