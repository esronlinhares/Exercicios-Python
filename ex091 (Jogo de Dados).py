from random import randint
from time import sleep
from operator import itemgetter
j = {'jogador1': randint(1,6),
     'jogador2': randint(1, 6),
     'jogador3': randint(1, 6),
     'jogador4': randint(1, 6)}
r = list()
print('Valores sorteados:')
for k, v in j.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
r = sorted(j.items(), key=itemgetter(1), reverse=True)
print('RANKING DOS JOGADORES:')
for i, v in enumerate(r):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)