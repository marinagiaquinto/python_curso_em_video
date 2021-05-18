print('PROGRESSÃO ARITMÉTICA')
print('-'*20)
n = int(input('Escolha um número: '))
r = int(input('Escolha a razão: '))

c = 1
cont = 0
while c <= 10:
    print(n, ' -> ', end=' ')
    n = n+r
    c += 1
print('Pausa')
mais = int(input('Deseja ver mais quantos termos da P.A? '))

c2 = 1
while c2 <= mais:
    print(n, ' -> ', end=' ')
    n = n+r
    c2 +=1
    if c2 > mais:
        print('Pausa')
        mais = int(input('Deseja ver mais quantos termos da P.A? '))
        c2 = 1
        if mais == 0:
            print('Fim do programa')
            c2 > mais
