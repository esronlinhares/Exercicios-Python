from datetime import date

nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano = date.today().year - nascimento

if ano <= 9:
    print('{} anos. Categoria Mirim.'.format(ano))
elif ano <= 14:
    print('{} anos. Categoria Infantil.'.format(ano))
elif ano <= 19:
    print('{} anos. Categoria Júnior.'.format(ano))
elif ano <= 25:
    print('{} anos. Categoria Sênior.'.format(ano))
else:
    print('{} anos. Categoria Master.'.format(ano))