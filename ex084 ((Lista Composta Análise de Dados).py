dados = []
pessoa = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoa) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoa.append(dados[:])
    dados.clear()
    d = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if d in 'Nn':
        break
print(f'Foram cadastradas {len(pessoa)} pessoas.')
print(f'O maior peso foi {maior} Kg. Peso de ', end='')
for p in pessoa:
    if p[1] == maior:
        print(f'{p[0]}.')
print(f'O menor peso foi {menor} Kg. Peso de ', end='')
for p in pessoa:
    if p[1] == menor:
        print(f'{p[0]}.')