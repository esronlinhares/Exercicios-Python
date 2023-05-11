velocidade = float(input('Qual a velocidade ataul do carro? '))
multa = (velocidade - 80) * 7
print('Você foi multado no valor de R$ {:.2f}.'.format(multa) if velocidade > 80 else 'Prossiga com segurança.')