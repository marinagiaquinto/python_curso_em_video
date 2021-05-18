palavras = (str(input('Digite uma palavra: ')),
            str(input('Digite outra palavra: ')),
            str(input('Digite a última palavra: ')))


c=0

for c in palavras:
    print(f'\nNa palavra {c.upper()} temos as vogais:', end=' ')
    for cont in c:
        if cont.lower() in 'aeiou':
            print(cont, end=' ')

#isso porque cada palavra na tupla é uma lista. Então percorremos a lista de cada nome printando as vogais.