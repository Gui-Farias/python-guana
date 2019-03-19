'''
Escreva umprograma que converta uma temperatura digitada em °C e converta para °F
'''

c = float(input('Difgite a temperatura em °C: '))
f = (c*9/5) +32
k = c + 273.15
print('{}°C corresponde a {}°F'.format(c,f))
print('{}°C corresponde a {}°K'.format(c,k))