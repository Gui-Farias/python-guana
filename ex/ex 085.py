'''
Crie um programa onde o usuario digite sete valores numericos cadstre em uma lista
que mantenha separados os valores pares e impares
- mostre os valore spares e impares em ordem crescente
'''

numeros = [[], [], []]

for x in range(0, 7):
    numeros[2].append(int(input(f'Digite o {x+1} Valor: ')))
    if numeros[2][x] % 2 == 0:
        numeros[0].append(numeros[2][x])
    else:
        numeros[1].append(numeros[2][x])
print(f'Os numeros digitados foram {numeros[2]}\nOs pares são {sorted(numeros[0])}\nOs impares são {sorted(numeros[1])}')
