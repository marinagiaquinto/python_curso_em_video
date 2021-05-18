from random import randint

print('VAMOS JOGAR PAR OU ÍMPAR!!!')
print('O jogo só para quando você perder!')
print('~'*45)
jogada = sorteio = c = 0

while True:
    n = int(input('Escolha um número: '))

    while True:
        jogada = str(input('Você escolhe par (p) ou ímpar (i): ')).strip().lower()
        if jogada != 'p' and jogada != 'i':
            print('Valor incorreto.')
        else:
            break

    sorteio = randint(0,11)
    print(f'Você escolheu {n} e eu {sorteio}, o total foi {n+sorteio}')

    if (n + sorteio) % 2 == 0 and jogada == 'p':
        print('PARABÉNS!!! O número é PAR!')
        print('Vamos jogar novamente.')
        print('~' * 30)
        c+=1
    elif (n + sorteio) % 2 != 0 and jogada == 'i':
        print('PARABÉNS!!! O número é ÍMPAR!')
        print('Vamos jogar novamente.')
        print('~'*30)
        c+=1
    else:
        print('~' * 30)
        print('VOCÊ ERROU !! GAME OVER !!')
        break
print(f'Você venceu {c} vezes. ')
print('~' * 30)