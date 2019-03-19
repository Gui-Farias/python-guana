'''
Crie u,a tupla com os 20 primeiros colocados da tebela do campeonato brasileiro de  futebol
- apenas os 5 primeiros colocados
- os ultimos 4 colocado
- uma lista com os times em ordem alfabetica
-  a posição da chapecoense
'''

camp = 'Palmeiras', 'Flamengo', 'Internacional','Grêmio', \
       'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', \
       'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', \
       'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná'

print(f'Os 5 primeiros colocados são:\n{camp[0:5]}')
print(f'Os 4 Ultimos foram \n{camp[-4:]}')
print(f'Os times na ordem alffabetica:\n{sorted(camp)}')
print(f'A chapeco ficou em {camp.index("Chapecoense")+1} ')
