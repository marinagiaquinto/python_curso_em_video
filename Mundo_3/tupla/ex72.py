listagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezevone', 'vinte')

while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if 0 < numero and numero > 20:
        print('Valor fora do intervalo pedido.')
    else:
        print(f'Você digitou o número {listagem [numero]}')
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if resp == 'N' or resp == 'NAO' or resp == 'NÃO':
            print('Fim de jogo.')
            break

