maior = homem = mulher = 0
while True:
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()
    d = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if i >= 18:
        maior += 1
    if s in 'Mm':
        homem += 1
    if s in 'Ff' and i < 20:
        mulher += 1
    if d in 'Nn':
        break
print(f'{maior} pessoas tem mais de 18 anos.')
print(f'{homem} homens foram cadastrados.')
print(f'{mulher} mulheres tem menos de 20 anos.')