tot = c = caro = ncaro = 0
cont = 'S'

while cont == 'S':
    np = (str(input('Nome do produto: ')))
    v = (float(input('Valor do produto: ')))
    tot += v
    if v > 1000:
        c+=1
    if v > caro:
        caro = v
        ncaro = np
    while True:
        cont = (str(input('Deseja continuar [S/N]? '))).strip().upper()
        if cont != 'N' and cont != 'S':
            print('Opção inválida.')
        else:
            break

print('-'*30)
print(f'Total gasto na compra foi R${tot} ')
print(f'{c} produto(s) custa(m) mais de R$1000')
print(f'{ncaro} foi o produto mais caro da compra.')

