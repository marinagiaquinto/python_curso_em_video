from random import choice
from time import sleep

print('Vamos jogar!!!')
escolhido = int(input('Vou pensar em um número de 0 a 5, adivinhe qual é: '))

lista = [1, 2, 3, 4, 5]
sorteio = choice(lista)

print('Processando...')
sleep(2)

if escolhido == sorteio:
    print(f'PARABÉNS!!!! você acertou!')
else:
    print(f'Puxa, você errou! :(')
    print(f'O número que pensei foi o {sorteio}. Fica pra próxima.')
