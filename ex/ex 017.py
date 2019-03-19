''''
Faça um porgama que leia o comprimento do cateto adjacente de um triangulo retangulo , calcule e mostre
o comprimento da hipotenusa
'''

from math import hypot

catopo = float(input('Digite o valor do Cateto Oposto: '))
catadj = float(input('Digite o valor do Cateto Adjacente '))
print('O valor da hipotenusa de um triangulo com cateto Oposte de {} e Cateto Adjacente de {} é de {:.2f}'.format(catopo,catadj,hypot(catopo,catadj)))

print('O valor da hipotenusa é {:.2f}'.format((catopo**2 + catadj**2)**(1/2)))
