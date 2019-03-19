'''
Faça um programa que leia 5 valores e guarde em uma lista
No final mostre qual foi o maior e o menor valor e sua posição na lista
'''

valor = []
maior = menor = 0

for x in range(0, 5):
    valor.append(int(input(f'Digite o {x+1} valor: ')))
    if x == 1:
        maior = menor = valor[x]
    else:
        if valor[x] > maior:
            maior = valor[x]
        if valor[x] < menor:
            menor = valor[x]


print(f'Os valores digitados foram: {valor}')
print(f'O Maior valor foi {max(valor)} e ele esta na posição {valor.index(max(valor))+1}')
print(f'O menor valor foi {min(valor)} e ele esta na posição {valor.index(min(valor))+1}')
print('-='*40)
print(f'O mairo valor digitado foi {maior} nas posiçoes: ' , end=' ')
for x, v in enumerate(valor):
    if v == maior:
        print(f'{x}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posiçoes: ', end=' ')
for x, v in enumerate(valor):
    if v == menor:
        print(f'{x}...', end=' ')