'''
Crie um programa que mostre todos os numeros pares que estão entre 1 e 50
'''

for x in range(1,51):
    if x % 2 == 0:
        print(x, end =' ')

for x in range(0, 51,2):
    print(x, end=' ')
