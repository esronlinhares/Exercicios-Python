s = mil = menor = c = 0
barato = ''
while True:
    n = str(input('Produto: '))
    i = float(input('Preço: '))
    c += 1
    s += i
    d = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if i > 1000:
        mil += 1
    if c == 1 or i < menor:
        menor = i
        barato = n
    if d in 'Nn':
        break
print(f'O total a pagar será R$ {s:.2f}.')
print(f'{mil} produtos custaram mais de R$ 1000,00.')
print(f'O produto mais barato foi {barato}.')