from datetime import date
ano = date.today().year

nascimento = (int(input('Digite o ano em que você nasceu: ')))

idade = ano - nascimento
tempo = 18 - idade
atrasado = idade - 18

if idade < 18:
    print('Você ainda não está no período de se alistar.')
    print(f'Mas atenção! Faltam {tempo} anos para seu alistamento!')
elif idade == 18:
    print('ATENÇÃO! Precisa se apresentar neste ano ao serviço militar!')
else:
    print(f'CORRA!!! VOCÊ JÁ DEVERIA TER SE APRESENTADO HÁ {atrasado} ANOS PARA O SERVIÇO MILITAR!')