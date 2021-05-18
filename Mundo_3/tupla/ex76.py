print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}') #com 40 casas e a escrita centralizada
print('-'*40)

listagem = ('Lápis', '1,75',
            'Borracha', '2,00',
            'Caderno', '15,90',
            'Estojo', '25,00',
            'Transferidor', '4,20',
            'Compasso', '9,99',
            'Mochila', '120,32',
            'Canetas', '22,30',
            'Livro', '34,90')

for c in range(0, len(listagem)):
    if c%2 == 0: # LEMBRANDO QUE A CONTAGEM COMEÇA COM 0
        print(f'{listagem[c]:.<30}', end=' ') #30 casas ocupadas com pontos à direita
    else:
        print(f'R$ {listagem[c]:>5}')
print('-'*40)

