'''
Aprimore o desafio anterior
- a soma de todos os valores pares
- a soma dos valores da terceira coluna
- o maior valor na segunda linha
'''

lista = [[], [], []]
soma = 0

for x in range(0, 3):
    for z in range(0, 3):
        lista[x].append(int(input('Digite um valor: ')))
        if lista[x][z] % 2 ==0:
            soma += lista[x][z]
for x in range(0, 3):
    for z in range(0, 3):
        print(f'{lista[x][z]}', end=' ')
    print(end='\n')


print(f'A soma dos valores pares é: {soma}')
print(f'A soma dos valores da terceira colune é: {lista[0][2]+lista[1][2]+lista[2][2]}')
print(f'O maior valor digitado na segunda linha foi: {max(lista[1])}')