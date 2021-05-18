id18 = m = f20 = 0

print('-'*10)
print('CADASTRO')
print('-'*10)

while True:
    id = (int(input('Idade: ')))
    if id > 18:
        id18 += 1
    while True:
        sexo = (str(input('Sexo [M/F]: '))).strip().upper()
        if sexo != 'M' and sexo != 'F':
            print('Valor incorreto.')
        elif sexo == 'M':
            m+=1
            break
        elif sexo == 'F':
            if id < 20:
                f20 += 1
            break

    cont = (str(input('Deseja continuar[S/N]? '))).strip().upper()
    if cont == 'N':
            break
    print('~~'*15)

print('-'*25)
print(f'Você cadastrou:')
print(f' {id18} pessoa(s) maiores de 18 anos.')
print(f' {m} homen(s).')
print(f' {f20} mulhere(s) menor(es) de vinte anos.')