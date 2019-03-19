'''
Crie um programa onde o usuario possa digitar cinco valores numericos e adicione na lista
ja na posição correta de inserção cresente,
no final mostre a lista ordenada
'''

valor = []

for x in range(0, 5):
    temp = int(input(f'Digite o {x} valor: '))
    if  x == 0 or temp > valor[-1]:
        valor.append(temp)
        print('Valor adicional ao final da lista!')
    else:
        pos = 0
        while pos < len(valor):
            if temp <= valor[pos]:
                valor.insert(pos, temp)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitado foram {valor}')