l = ('Lápis', 1.75,
     'Borracha', 2,
     'Caderno', 15.90,
     'Estojo', 120,
     'Canetas', 22.30,
     'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for c in range(0, len(l)):
    if c % 2 ==0:
        print(f'{l[c]:.<30}', end='')
    else:
        print(f'R$ {l[c]:>7.2f}')
print('-'*40)