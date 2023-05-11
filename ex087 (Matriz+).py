m = [[0,0,0], [0,0,0], [0,0,0]]
par = col = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}]', end='')
        if m[l][c] % 2 == 0:
            par += m[l][c]
    print()
print(f'A soma dos valores pares é {par}.')
for l in range(0, 3):
    col += m[l][2]
print(f'A soma dos valores da terceira coluna é {col}.')
for c in range(0, 3):
    if c == 0:
        maior = m[1][c]
    elif m[1][c] > maior:
        maior = m[1][c]
print(f'O maior valor da segunda linha é {maior}.')