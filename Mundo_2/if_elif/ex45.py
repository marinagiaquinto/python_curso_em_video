refazerrrrrrrrrrr


from random import randint
print('-------------------------')
print('         JOKEMPÔ         ')
print('-------------------------')
print('SEJA BEM VINDO, JOGADOR!')
print('Apresentando suas armas:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
print('---------------------------')
jogador = int(input('Faça sua escolha: '))

jogo = ['pedra','papel','tesoura']
computador = randint(0,2)

print(f'O computador escolheu {computador}')

if jogador == jogo:
    if jogador == 0:
        print(f'pedra x {jogo[computador]}: PARABÉNS COMPETIDORES, EMPATE !!!!')
    elif jogador == 1:
        print(f'papel x {jogo[computador]}: PARABÉNS COMPETIDORES, EMPATE !!!!')
    else:
        print(f'tesoura x {jogo[computador]}: PARABÉNS COMPETIDORES, EMPATE !!!!')
elif jogador == 0 and computador == 1:
    print(f'pedra x {jogo[computador]}: PUXA JOGADOR, ACABOU DE PERDER ESSA !!!!')
elif jogador == 0 and computador == 2:
    print(f'pedra x {jogo[computador]}: AEEEE ! PARABENS! VOCÊ É O GANHADOR!')
elif jogador == 1 and computador == 0:
    print(f'papel x {jogo[computador]}: AEEEE ! PARABENS! VOCÊ É O GANHADOR!')
elif jogador == 1 and computador == 2:
    print(f'papel x {jogo[computador]}: PUXA JOGADOR, ACABOU DE PERDER ESSA !!!!')
elif jogador == 2 and computador == 1:
    print(f'tesoura x {jogo[computador]}: AEEEE ! PARABENS! VOCÊ É O GANHADOR!')
elif jogador == 2 and computador == 0:
    print(f'tesoura x {jogo[computador]}: PUXA JOGADOR, ACABOU DE PERDER ESSA !!!!')
else:
    print('Opção inválida !!! Reinicie o jogo! :l')
