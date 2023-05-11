from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

if idade < 18:
    saldo = 18 - idade
    print('Falta(m) {} ano(s) para você se alistar.'.format(saldo))
elif idade == 18:
    print('Está na hora de você se alistar.')
else:
    saldo = idade - 18
    print('Você já passou do prazo de alistamento há {} ano(s).'.format(saldo))