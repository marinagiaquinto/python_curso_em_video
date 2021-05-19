from random import choice
a1 = input('Aluno um: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista_aluno = [a1, a2,a3,a4]
escolhido = choice(lista_aluno)
print(f'O aluno sorteado foi {escolhido}')

#random, biblioteca para gerar dados "aleatórios". Random choice, 1 escolha aleatória