from datetime import date

ano = int(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('{} é bissexto.'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))