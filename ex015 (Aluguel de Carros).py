km = float(input('Quantidade de km percorridos: '))
dia = int(input('Quantidade de dias alugado: '))
valor = (km*0.15) + (dia*60)
print('O valor a ser pago é: R$ {:.2f}'.format(valor))