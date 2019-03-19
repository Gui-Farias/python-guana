'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde os em uma tupla
- quantas vezes aparece o 9
- em que posição está o primeiro 3
- quais os numeros pares
'''

num = int(input('Digite um num: ')), int(input('Digite um num: ')), \
      int(input('Digite um num: ')),int(input('Digite um num: '))
print(f'Os numeros digitados foram: ', end='')
for n in num:
    print(f'{n}', end=' ')
print(f'\nOs numeros pares são: ', end=' ')
for n in num:
    if n %2 ==0:
       print(f'{n}', end=' ')
print(f'\nFoi digitado {num.count(9)} vezes o numero 9')
if 3 in num:
    print(f'O numero 3 aparece pela primeira vez na {num.index(3)+1} posição')
else:
    print('Não foi digitado o numero 3')
