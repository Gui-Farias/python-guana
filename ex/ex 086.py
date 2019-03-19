'''
Crie um program que crie uma matriz de 3x3 e preencha com valores lido pelo teclado
- mostre a matriz com a formatação correta
'''

lista = [[], [], []]
for x in range(0,3):
    for z in range(0,3):
        lista[x].append(int(input('Digite um valor: ')))

for x in range(0,3):
    for z in range(0,3):
        print(f'[{lista[x][z]:^6}]', end=' ')
    print(end='\n')
