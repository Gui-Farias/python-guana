'''
Crie um programa que vai ler varios numeros e colcoar na lista
-quantos numeros foram digitados
-a lista de valores em ordem decresente
-se o 5 faz parte da lista e qual sua posição
'''

valor = []
cont = 0

while True:
    valor.append(int(input('Digite um valor: ')))
    cont += 1
    again = input('Deseja continuar? [S/N] ').strip().upper()
    if again != 'S':
        break

valor.sort(reverse=True)
print(f'Foram digitado {cont} numeros sendo eles em ordem decrescente: {valor}')
if 5 in valor:
    print('Tem sim o valor 5 na lista!')
else:
    print('Não foi digitado o valor 5 nenhuma vez!')
