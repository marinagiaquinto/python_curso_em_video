tot_id = 0
media = 0
nome_velho = ''
maior_id = 0
men_20 = 0

for c in range(1,5):

    nome = str(input(f'Digite o nome da {c}ª pessoa: ')).strip().lower()

    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    tot_id += idade

    sexo = str(input(f'Digite o sexo (M/F) da {c}ª pessoa: ')).strip().upper()
    if c == 1 and sexo == 'M':
        maior_id = idade
        nome_velho = nome
    if c != 1 and sexo == 'M' and maior_id < idade:
        maior_id = idade
        nome_velho = nome

    elif sexo == 'F' and idade < 20:
        men_20 += 1

    print('--------------------------------------------------')

media = tot_id/4

print(f'A média de idades do grupo é {media} ')
print(f'A idade do homem mais velho é {maior_id} e seu nome é {nome_velho}')
print(f'Existe(m) {men_20} mulhere(s) com idade menor de 20 anos.')
