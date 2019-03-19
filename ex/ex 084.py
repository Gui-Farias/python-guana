'''
Faça um programa que leia o nome e o peso de varias pessoas guardando em lista
- quantas pessoas foram cadastradas
- uma listagem com as pessoas mais pesadas
- uma listagem com as pessoas mais leves
'''

lista = []
listajunta = []
pesado = []
pena = []
cont = 0
while True:
    cont += 1
    listajunta.append(input('Digite o seu nome: '))
    listajunta.append(float(input('Digite o seu peso: ')))
    again = input('Deseja continuar? [S/N]').upper().strip()
    lista.append(listajunta[:])
    listajunta.clear()
    if cont == 1 :
        pesado = listajunta
    if lista[-1][1] >= 100:
        pesado.append(lista[-1])
    elif lista[-1][1] <= 50:
        pena.append(lista[-1])
    while again not in 'SN':
        again = input('Deseja continuar? [S/N] ').upper().strip()
    if again == 'N':
        break

print(f'Ao todo foram cadastrados {cont} pessoas!')
if len(pesado) > 0:
    print('\nAs pessoas com mais de 100KG foram:\n')
    for x in pesado:
        print(f'{x[0]} com {x[1]:.2f}KG')
else:
    print('\nNão teve ninguem com mais de 100KG')
if len(pena) > 0:
    print('\nAs pessoas com menos de 50KR foram:\n')
    for x in pena:
        print(f'{x[0]} com {x[1]:.2f}KG')
else:
    print('\nNão teve ninguem com menos de 50KG')
