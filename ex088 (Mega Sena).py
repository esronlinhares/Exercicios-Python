from random import randint
from time import sleep
lista = []
jogos = []
q = int(input('Quantos jogos você quer sortear? '))
t = 1
while t <= q:
    c = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            c += 1
        if c >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    t += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {sorted(l)}')
    sleep(1)