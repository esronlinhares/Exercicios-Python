p = 'S'
c = s = m = maior = menor = 0
while p in 'Ss':
    n = int(input('Digite um número: '))
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    p = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
m = s / c
print('Você digitou {} números e a média foi: {}.'.format(c, m))
print('O maior número foi {} e o menor foi {}.'.format(maior, menor))