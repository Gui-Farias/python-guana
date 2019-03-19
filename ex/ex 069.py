'''
Crie um programa que leie a idade e o sexo de varias pessoas
a cada pessoa cadastrada devera perguntar se o usuario quer continuar no final mostr:
- Qaunatas pessoas tem mais de 18 anos
- quantos homens foram cadasrrtrado
- quantas mulheres tem menos de 20 anos
'''

maior = men = novamulher = pesq = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = ''
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Qual o seu sexo [M/F]? ')).upper().strip()
    if sexo == 'M':
        men += 1
    if idade > 18:
        maior += 1
    if sexo == 'F' and idade < 20:
        novamulher +=1
    pesq += 1
    continua = str(input('\n\033[36mDeseja conitnuar?\033[m')).upper().strip()
    if continua != 'S' and continua != 'SIM':
        break

print(f'o cadastro foi feito com {pesq} pessoas:\n{maior} pessoas tem mais de 18 anos\n{men} homem foram cadastrado\n{novamulher} mulherees tem menos de 20 anos')