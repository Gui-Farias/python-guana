'''
Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores M ou F
caso esteja errado peça a digitação novamente até ter um valor correto
'''

sexo = ' '
while sexo not in 'MF':
    sexo = str(input('Digite o seu sexo M ou F ')).upper().strip()

print('Sexo {} escolhido!'.format(sexo))
