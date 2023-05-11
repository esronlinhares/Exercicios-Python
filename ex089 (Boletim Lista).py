f = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    f.append([nome, [n1, n2], media])
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for i, a in enumerate(f):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    p = int(input('Mostrar notas do aluno [999 para]: '))
    if p == 999:
        print('Finalizando.')
        break
    if p <= len(f):
        print(f'Notas de {f[p][0]} são {f[p][1]}.')