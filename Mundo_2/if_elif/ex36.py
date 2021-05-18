casa = float(input('Qual o valor da casa que deseja comprar? '))
salario = float(input('Qual o valor da seu salário? '))
anos = int(input('Deseja pagar a casa em quantos anos? '))

parcela = casa / (anos*12)
comprometido = (parcela*100)/salario
maximo = (salario / 100) * 30

print(f'O valor da sua parcela seria de: {parcela :.2f} ')
print(f'Isso representaria {comprometido :.2f} porcento do seu salário. ')

if parcela <= maximo:
    print('Parabéns!!! Seu empréstimo foi aprovado!')
else:
    print('Lamento muito. Seu empréstimo foi negado.')
print('Agradecemos muito a sua vinda.')
