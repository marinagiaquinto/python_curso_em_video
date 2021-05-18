from random import choice

print('--------------------')
print('VAMOS JOGARRRR !!!!')
print('--------------------')

print('Estou pensando em um número de 0 a 10')
numero = int(input('Será que você consegue advinhar? Seu chute: '))

lista = [0,1,2,3,4,5,6,7,8,9,10]
sorteio = choice(lista)

c=1
while sorteio != numero:
    if numero < sorteio:
        numero = (int(input('Mais. Tente de novo: ')))
        c += 1
    if numero > sorteio:
        numero = (int(input('Menos. Tente de novo: ')))
        c += 1
print(f'PARABÉNSSS!!! VOCÊ ACERTOU em {c} tentativas. ')