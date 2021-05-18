frase = str(input('Escreva uma frase: ')).strip().lower()

palavras = frase.split()
tudojunto = ''.join(palavras)
inverso = tudojunto [::-1]

print('---------------------')
print(tudojunto)
print(inverso)
print('---------------------')

if tudojunto == inverso:
    print('Esta frase é um palindromo')
else:
    print('Esta frase não é um palindromo')