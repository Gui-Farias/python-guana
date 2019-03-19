'''
Crie um programa que leia varios numeros interios pelo teclado
o programa so vai parar quando o usuairo digitar 999
no final mostre quantos nuemros foram digitadoe e qual foi a soma entre eles
'''

soma = cont = 0

while True:
    num = int(input('Digite um valor (pare com 999): '))

    if num == 999 and cont == 0:
        print('Não foi digitado nem um outro numero alem do de parar "999"')
        break
    elif num == 999:
        break
    soma += num
    cont += 1

if cont != 0:
    print(f'Foram digitados {cont} Numero e a a soma entre eles é {soma}!')
