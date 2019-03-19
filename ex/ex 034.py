'''
Escreva um programa  que pergunte o salario de um funcionario e calcule o valor do sue aumento
para salarios superiores a R$1250.00 calcule um aumento de 10%
para inferior ou igual o aumento é de 15%
'''

salario = float(input('Digite o seu salario para calcular o seu aumento: '))

if salario <= 1250.00:
    newsalario = salario * 1.15
    print('o seu novo salario vai ser R${:.2f}'.format(newsalario))
else:
    newsalario = salario *1.10
    print('O seu novo salario vai ser R${:.2f}'.format(newsalario))
