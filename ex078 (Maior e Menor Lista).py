v = []
for c in range(0, 5):
    v.append(int(input('Digite um valor: ')))
print(f'Você digitou os valores {v}.')
print(f'O maior número foi {max(v)} nas posições ', end='')
for i, p in enumerate(v):
    if p == max(v):
        print(f'{i} ', end='')
print(f'\nO menor número foi {min(v)} nas posições ', end='')
for i, p in enumerate(v):
    if p == min(v):
        print(f'{i} ', end='') 