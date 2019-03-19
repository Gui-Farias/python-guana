'''
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados['sexo'])
del dados['idade']
print(dados)

filme = {
    'titulo': 'StarWars', 'ano': 1977, 'diretor': 'GeorgeLucas'

}

print(filme.values())  # pega os valores
print(filme.keys())  # pega o indificador
print(filme.items())  # printa tudo

for k, v in filme.items():
    print(f'O {k} é {v}')

pessoas = {
    'nome': 'Gustavo', 'sexo': 'M', 'idade': 22
}

print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(f'{pessoas.keys()}')
print(f'{pessoas.values()}')
print(f'{pessoas.items()}')

for k, v in pessoas.items(): # similiar ao enumerate das listas
    print(f'{k} = {v}')

del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5

for k, v in pessoas.items():
    print(f'{k} = {v}')


brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
'''

estado = {}
brasil = []
for x in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())  #.copy parecido com o [:] das listas
for e in brasil:
    print(f'{e}')
    print('-'*30)
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
