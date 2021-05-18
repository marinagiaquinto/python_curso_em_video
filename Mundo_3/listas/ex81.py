numeros = []
decisao = 'sim'

while decisao[0] != 'N':
    numeros.append(int(input('Digite um número: ')))
    while True:
        decisao = (str(input('Deseja continuar[S/N]? '))).strip().upper()
        if decisao != 'S' and decisao != 'SIM' and decisao != 'N' and decisao != 'NAO' and decisao != 'NÃO':
            print('Opção inválida.')
        else:
            break
    print('-'*20)
print('-//-'*10)

print(f'Foram digitado {len(numeros)} números.')

numeros.sort(reverse = True)
print(f'Seus valores, em ordem decrescente, são: {numeros}')

if 5 in numeros:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')