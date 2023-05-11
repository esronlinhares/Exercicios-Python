l = []
par = []
impar = []
while True:
    l.append(int(input('Digite um valor: ')))
    d = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if d in 'Nn':
        break
for i, v in enumerate(l):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa é {l}.')
print(f'A lista de pares é {par}.')
print(f'A lista de ímpares é {impar}.')