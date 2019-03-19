lanche = 'hamburgue', 'suco', 'pizza',  'pudim'

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na poosição {cont}')

for pos, comida in enumerate(lanche):
    print(f'ej vou comer {comida} na posição {pos}')

print('Eu comi de mais')

print(sorted(lanche))


a = 2, 5, 4
b = 5, 8, 1, 2
c = a + b
print(c)
print(len(c))
print(c.count(2))
print(c.index(5))
print(c.index(5, 2))

pessoa = 'Gui', 18, 'M', 60
del(pessoa)
print(pessoa)

