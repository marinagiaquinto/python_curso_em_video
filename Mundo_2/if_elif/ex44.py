compra = float(input('Qual o valor da sua compra? R$ '))
print('-------------------------------------------')
print('           FORMAS DE PAGAMENTO:            ')
print('-------------------------------------------')
print('[1] à vista dinheiro/cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço formal')
print('[4] 3x ou mais no cartão: 20% de juros')
print('---------------------------------------------')
pagamento = int(input('Digite a forma de pagamento desejada: '))

if pagamento == 1:
    valor = compra - (compra*10/100)
elif pagamento == 2:
    valor = compra - (compra*5/100)
elif pagamento == 3:
    valor = compra
    parcela = valor/2
    print(f'O valor mensal da sua compra será de {parcela}')
elif pagamento == 4:
    valor = compra + (compra*20/100)
    parcela = int(input('Em quantos meses deseja dividir sua compra? '))
    mes = valor/parcela
    print(f'O valor da sua parcela será de {mes}')
else:
    print('Opção inválida. Reinicie o processo.')

print(f'O valor total da sua compra que era de {compra} e passou a ser de {valor :.2f}.')
