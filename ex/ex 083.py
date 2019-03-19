'''
Crie um prgrama onde o usuario digite uma expressao qualquer que use parenteses
seu app devera analiizar se a expressao está com os parenteses abertos e fechados na ordem correta
'''

ex = input('Digite sua expressão: ')
lista = []

for x in ex:
    if x == '(':
        lista.append(x)
    elif x == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(x)
            break
if len(lista) == 0:
    print(f'\033[0;36mA expressão {ex} é valida!!')
else:
    print(f'\033[0;31m"{ex}" NÃO é um expressão valida!!')
