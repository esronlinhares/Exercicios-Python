n = [[], []]
for c in range(1, 8):
    v = int(input(f'Digite o {c}º valor: '))
    if v % 2 == 0:
        n[0].append(v)
    elif v % 2 == 1:
        n[1].append(v)
print(f'Os valores pares são: {sorted(n[0])}')
print(f'Os valores ímpares são: {sorted(n[1])}')