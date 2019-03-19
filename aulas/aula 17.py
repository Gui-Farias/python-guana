lanche = ['hamburgue', 'suco', 'pizza', 'sorvete']
lanche.append('cookei')  #ADICIONA NO FINAL DA LISTA
lanche.insert(0, 'hot-dog')  #ADICIONA ONDE VOCE QUISER, SENDO O PRIMEIOR VALOR O INDECE QUE DESEJA
print(lanche)

del lanche[3]
lanche.pop(3)
lanche.remove('hot-dog')
print(lanche)
lanche.pop()  #Remove o ultimo indice

valor = list(range(4,11))

print(valor)

valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)

valores.sort()
print(valores)

valores.sort(reverse=True)
print(valores)

print(len(valores))

lista = []
for cont in range(0,5):
    lista.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a  #ligação de lista
b = a[:]  #copia de valores
b[2] = 8

print(f'Lista A {a}\nLista B {b}')
