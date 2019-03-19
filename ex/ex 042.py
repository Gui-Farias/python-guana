'''
refaça o ex 035 e acresente qual triangulo sera formado
- Equilatero: todos os lados igual
- Isosceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''

print('-='*20, '\nAnalizador de triangulos 2.0\n' + '-='*20)
reta1 = float(input('Digite o primeiro segmento: '))
reta2 = float(input('Digite o segundo segmento: '))
reta3 = float(input('Digite o terceiro segmento: '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('É possivel formar um triangulo e esse triango sera um: ', end='')
    if reta1 == reta2 == reta3:
        print('\033[0;33mEquilatero')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('\033[0;32mIsosceles')
    else:
        print('\033[0;31mEscaleno')
else:
    print('Não é possivel formar um triangulo com esses segmnetos.')
