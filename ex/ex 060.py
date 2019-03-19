'''
faça um programa que leia um nuermo qualquer e msotre o seu fatorial
ex
5! = 5x4x3x2x1 = 120
'''

num = int(input('Digite um numero: '))
expo = num
print(num)

while num != 1:
    print(' {} x {} x'.format(expo, num -1), end=' ')
    expo = expo * (num - 1)
    num -= 1

print(expo)


