g = []
p = {}
soma = media = 0
while True:
    p.clear()
    p['nome'] = str(input('Nome: '))
    while True:
        p['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if p['sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F.')
    p['idade'] = int(input('Idade: '))
    soma += p['idade']
    g.append(p.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('Erro! Digite S ou N.')
    if r == 'N':
        break
print('-'*30)
print(f'A) Ao todo temos {len(g)} pessoas cadastradas.')
media = soma / len(g)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in g:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in g:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('Encerrando.')