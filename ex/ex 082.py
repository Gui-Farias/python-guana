'''
Crie um programa que via ler varios numeors e colocar na lista
depois disso crie duas lista extrar que vao conter apenas os valores pares e os impares
mostre o conteudo das tres listas
'''

valor = []
par = []
impar = []
nulo = 0

while True:
    valor.append(int(input('Digite um valor: ')))
    again = input('Deseja continuar? [S/N}').strip().upper()
    if again != 'S':
        break

print(f'Os valores digitados foram: {valor}')

for x in valor:

    if x == 0:
        nulo += 1
    elif x % 2 ==0:
        par.append(x)
    else:
        impar.append(x)

print(f'Sendo que os valores pares foram \033[0;34m{par}\033[m\nE os impares \033[0;32m{impar}\033[m')
if nulo > 0:
    print('Tambem foi digitado o "\033[1;36mZERO\033[m"')
