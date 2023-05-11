from random import randint
v = 0
while True:
    j = int(input('Digite um número: '))
    e = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    c = randint(0, 10)
    total = c + j
    if e == 'P':
        if total % 2 == 0:
            print(f'Você jogou {j} e o computador jogou {c}.')
            print('Você venceu!')
            v += 1
        else:
            print(f'Você jogou {j} e o computador jogou {c}.')
            print('Você perdeu!')
            break
    if e == 'I':
        if total % 2 == 1:
            print(f'Você jogou {j} e o computador jogou {c}.')
            print('Você venceu!')
            v += 1
        else:
            print(f'Você jogou {j} e o computador jogou {c}.')
            print('Você perdeu!')
            break
print(f'GAME OVER! Você venceu {v} vezes.')