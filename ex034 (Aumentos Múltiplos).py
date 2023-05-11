salario = float(input('Qual seu salário? '))
if salario <= 1250:
    print('Seu novo salário é R$ {:.2f}'.format(salario+(salario*0.15)))
else:
    print('Seu novo salário é R$ {:.2f}'.format(salario+(salario*0.10)))