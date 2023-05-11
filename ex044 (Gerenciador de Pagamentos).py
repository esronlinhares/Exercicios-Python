valor = float(input('Digite o valor do produto: '))
print('''Escolha a opção de pagamento:
[1] À vista em dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Informe a opção de pagamento: '))

if opcao == 1:
    print('O valor a ser pago será: R$ {}'.format(valor - (valor*0.10)))
elif opcao == 2:
    print('O valor a ser pago será: R$ {}'.format(valor - (valor*0.05)))
elif opcao == 3:
    print('O valor a ser pago será: R$ {}'.format(valor))
elif opcao == 4:
    print('O valor a ser pago será: R$ {}'.format(valor + (valor*0.20)))
else:
    print('Opção inválida.')