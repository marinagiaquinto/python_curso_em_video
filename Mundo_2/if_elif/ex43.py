peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc= peso/(altura*altura)
print(f'Seu imc é {imc :.1f}. Você está ', end='')

if imc < 18.5:
    print('abaixo do peso.')
elif 18.5 <= imc < 25:
    print('no peso ideal.')
elif 25 <= imc < 30:
    print('com sobrepeso.')
elif 30<= imc < 40:
    print('obeso.')
else:
    print('com obesidade mórbida.')

