teste = []
teste.append('Guilherme')
teste.append(18)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['joao', 19], ['Ana', 33], ['Jpoaquim', 13], ['Maria', 45]]
print(galera[0][1])
print(galera[1][0])
print(galera[3])
print('-='*20)
for x in galera:
    print(x)
print('-='*20)
for x in galera:
    print(f'{x[0]}, tem {x[1]} Anos de idade!')








galera = []
galera1 = []
dado = []
maior = menor = 0
for x in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    galera1.append(dado)
    dado.clear()
print('-='*30)
print(galera)
print(galera1)

for x in galera:
    if x[1] >= 21:
        print(f'{x[0]} é maior de idade!')
        maior += 1
    else:
        print(f'{x[0]} é menor de idade')
        menor +=1
print(f'Temos {maior} maiores de idade e {menor} menores de idade')
