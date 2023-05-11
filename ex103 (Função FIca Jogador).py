def ficha(j='', gol=0):
    print(f'O jogador {j} fez {gol} gols no campeonato.')
    
    
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g) 
