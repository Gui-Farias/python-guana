'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quaantas vezes a aprece a letra 'A'
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela ultima vez
'''

frase = input('Digite uma frase: ').upper().strip()
print('A letra "A" aparece {} vezes na frase "{}"'.format(frase.count('A'), frase))
print('O A apreceu primeio na posição {} e por ultimo na posição {}'.format(frase.find('A')+1, frase.rfind('A')+1))
