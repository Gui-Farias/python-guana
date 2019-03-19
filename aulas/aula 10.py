
'''
tempo = int(input('Qauntos anos tem sue carro? '))
if  tempo <=3:
    print('Carro Novo')
else:
    print('Carro velho')
print('--FIM--')

print('Carro novo' if tempo<=3 else'Carro velho')


nome = str(input('Qual é o sue nome? '))
if 'Guilherme' in nome:
    print('Que nome lindo você tem!')
else:
    print('Que nome mais normal kkk!')
print('Bom dia, {}'.format(nome))


'''


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua media foi {:.1f}'.format(m))
if m >=6.0:
    print('Sua media foi boa! PARABENS!!')
else:
    print('Sua medua foi horrivel! Vai estudar')
print('PARABENS' if m >=6 else 'Estude mais')
