from datetime import date
anoatual = date.today().year

anonasc = (int(input('Digite seu ano de nascimento: ')))
idade = anoatual - anonasc

print(f'Você possui {idade} anos.')

if idade <= 9:
    print('Você está na categoria MIRIM.')
elif idade <= 14:
    print('Você está na categoria INFANTIL.')
elif idade <= 19:
    print('Você está na categoria JÚNIOR.')
elif idade <= 25:
    print('Você está na categoria SÊNIOR.')
else:
    print('Você está na categoria MASTER.')

#Tiramos a condição  9> idade <= 14 porque a condição já está acima.
#Ou seja, se passou para a condição de baixo foi porque as anteriores não foram atendidas.