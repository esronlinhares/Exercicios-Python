l = []
while True:
    l.append(int(input('Digite um valor: ')))
    d = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if d in 'Nn':
        break
print(f'Foram digitados {len(l)} números.')
l.sort(reverse=True)
print(f'A lista em ordem decrescente é: {l}.')
if 5 in l:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')