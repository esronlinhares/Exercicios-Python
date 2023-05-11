p = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while p not in 'MmFf':
    if p != 'M' or 'F':
        p = str(input('Sexo inválido. Digite seu sexo novamente [M/F]: ')).strip().upper()
print('Sexo {} registrado com sucesso.'.format(p))