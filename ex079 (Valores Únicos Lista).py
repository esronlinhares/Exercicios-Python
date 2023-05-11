v = []
while True:
    n = int(input('Digite um valor: '))
    if n not in v:
        v.append(n)
        print('Valor adicionado.')
    else:
        print('Valor duplicado! Não vou adicionar.')
    d = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if d in 'Nn':
        break
print(f'Você digitou os valores {sorted(v)}.')