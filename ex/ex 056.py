'''
Desenvolva um programa que leia o nome idade e sexo da 4 pessoas. no final do programa  mostre:
- A media de idade do grupo
- qual pe o nome do homem mais velho
-quantas mulheres tem menso de 20 anos
'''

idade = 0
velho = ''
novamulher = 0
somaidade = 0
somaidadem = 0

for x in range(1,5):
    nome = str(input('Digite o sue nome: ')).strip()
    idade = int(input('Qual sua idade?: '))
    somaidade += idade
    sexo = str(input('Qual o seu sexo? M ou F?')).upper().strip()

    if sexo == 'M' and idade > somaidadem:
        somaidadem = idade
        velho = nome
    elif sexo == 'F' and idade < 20:
        novamulher += 1

print('\033[0;31mA media da soma de todas a s pessoas é de : {}\033[m\n\033[0;32mO homem mais velho é o {} com {} anos\033[m\n\033[0;35m{} mulheres tem menos de 20 anos.\033[m'.format(somaidade / 4, velho, somaidadem,novamulher))
