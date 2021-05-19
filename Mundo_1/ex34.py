salario = int(input('Digite seu salário: '))

if salario <= 1250:
    aumento = salario*15/100
    salario = salario + aumento
else:
    aumento = salario*10/100
    salario = salario + aumento

print(f'Seu salário passou a ter um aumento de {aumento :.2f} e passou a ser {salario :.2f}')