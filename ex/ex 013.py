'''
Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
'''

salario = float(input('Digite o seu salario ataul: '))
newsalario = salario + (salario*0.15)
print('O seu novo salario com aumento de 15% é de {:.2f} Reais'.format(newsalario))