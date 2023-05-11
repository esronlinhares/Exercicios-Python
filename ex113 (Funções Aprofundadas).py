def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('Erro! Digite um número inteiro válido.')
            continue
        except(KeyboardInterrupt):
            print('Usuário prefiriu não digitar.')
            return 0
        else:
            return n
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('Erro! Digite um número real válido.')
            continue
        except(KeyboardInterrupt):
            print('Usuário prefiriu não digitar.')
            return 0
        else:
            return n
n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')