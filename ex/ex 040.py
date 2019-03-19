'''
Crie um programa que leia duas notas de um aluno e calcula sua media mostrando uma mensagem no final
- media abaixo de 5.0 reprovado
-media entre 5.0 6.9 recuperção
- media 7.0 ou mais aprovado
'''

from time import sleep

nota1 = float(input('{}Digite sua primeira nota:{} '.format('\033[7;36m', '\033[m')))
nota2 = float(input('{}Digite sua seunda nota:{} '.format('\033[0;33m', '\033[m')))

med = (nota1 + nota2) / 2
print('\033[35m_-'*40)
print('Aguarde estamos calculando sua media e sua situação!!')
print('_-'*40,'\n\033[m')

sleep(3)
if med < 5.0:
    print('\033[7;30mVocê foi \033[1;31;40mreprovado\033[7;30m, media {} espero que ano que vem estudo mais!!!\033[m'.format(med))
elif med > 7.0:
    print('{}Parabens!!{}\nVocê passou de ano com media {}'.format('\033[1;32m', '\033[m', med))
else:
    print('è sua nota nao foi tao boa, vai ter que fazer uma recupeção para melhorar esse {} de media'.format(med))
