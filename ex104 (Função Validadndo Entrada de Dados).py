def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('Erro! Digite um número inteiro válido.')
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
