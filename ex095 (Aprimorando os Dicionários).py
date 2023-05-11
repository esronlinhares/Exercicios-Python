j = {}
p = []
t = []
while True:
    j.clear()
    j['nome'] = str(input('Nome do jogador: '))
    q = int(input(f'Quantas partidas {j["nome"]} jogou? '))
    p.clear()
    for c in range (1, q+1):
        p.append(int(input(f'Quantos gols na partida {c}? ')))
    j['gols'] = p[:]
    j['total'] = sum(p)
    t.append(j.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if r == 'N':
        break
print('-'*40)
print('cód. ', end='')
for i in j.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(t):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    b = int(input('Mostrar dados de qual jogador? (999 interrompe)'))
    if b == 999:
        break
    if b >= len(t):
        print(f'Erro! Não existe jogador com código {b}!')
    else:
        print(f'Levantamento do jogador {t[b]["nome"]}: ')
        for i, g in enumerate(t[b]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
        print('-'*40)
print('Volte Sempre!')