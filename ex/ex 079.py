'''
Crie um programa onde o usuario possa digitar varios valores nuemricos,
e adiciona na lista caso não exista
no final mostrar todos os valores adicionada em ordem crescente
'''

valor = []

while True:
    temp = int(input('Digite um valor: '))
    if temp in valor:
        print('\033[0;31mValor ja contem na lsita! \033[m')
    else:
        valor.append(temp)
        print('\033[0;35mValor adicionadao na lista!\033[m')
    cont = input('Deseja continuar? [S/N]').upper()
    if cont != 'S':
        break

print(f'Os valores digitados foram: {sorted(valor)}')