'''
Crie um programa que leia dois valores e o mostre um menu na tela:
[1] somar
[2] mutiplicar
[3] maior
[4] novos numeros
[5] sair do programa
'''

escolha = 0
num1 = int(input('\nDigite um numero: '))
num2 = int(input('Digite outro numero: '))

while escolha != 5:

    escolha = int(input('\nAgora faça uma esoclha:\n[1] - Somar\n[2] - Multiplciar\n[3] - Mostrar o maior\n[4] - Digitar novos numeros\n[5] - Sair do programa:\n'))

    if escolha == 1:
        soma = num1 + num2
        print('A soma dos valores foi: {}'.format(soma))
    elif escolha == 2:
        mult = num1 * num2
        print('A multiplicação entre os numeros {} e {} da {}'.format(num1, num2, mult))
    elif escolha == 3:
        maior = num1
        if num2 > num1:
            maior = num2
        print('O maior numero é o {}'.format(maior))
    elif escolha == 4:
        num1 = int(input('\nDigite um numero: '))
        num2 = int(input('Digite outro numero: '))
    elif escolha == 5:
        print('Finalizando o programa ...')
    else:
        print('Opção oinalida')