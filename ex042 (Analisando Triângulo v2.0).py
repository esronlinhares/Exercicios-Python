r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('As retas podem formar um triângulo ', end='')
    #if r1 == r2 and r2 == r3:
    if r1 == r2 == r3:
        print('equilátero.')
    #if r1 != r2 and r2 != r3
    elif r1 != r2 != r3 != r1:
        print('escaleno.')
    else:
        print('isóceles.')
else:
    print('As retas não podem formar um triângulo.')