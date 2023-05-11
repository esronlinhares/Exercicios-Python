d = {}
p = []
d['nome'] = str(input('Nome do jogador: '))
t = int(input(f'Quantas partidas {d["nome"]} jogou? '))
for c in range (1, t+1):
    p.append(int(input(f'Quantos gols na partida {c}? ')))
d['gols'] = p[:]
d['total'] = sum(p)
print('-'*30)
print(d)
print('-'*30)
for k, v in d.items():
    print(f'O campor {k} tem o valor {v}.')
print('-'*30)
print(f'O jogador {d["nome"]} jogou {len(d["gols"])} partidas.')
for i, v in enumerate(d['gols']):
    print(f'Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {d["total"]} gols.')