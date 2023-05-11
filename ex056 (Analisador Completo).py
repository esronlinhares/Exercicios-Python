media = 0
maior = 0
velho = 0
mulher = 0
for c in range(1, 5):
    print('----- {}ª Pessoa -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    media += idade / 4
    if c == 1 and sexo in 'Mm':
        maior = idade
        velho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1
print('A média de idade do grupo é: {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher))