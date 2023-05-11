from datetime import date
totmaior = 0
totmenor = 0
for c in range(1, 7):
    n = int(input('Em que ano a {}ª nasceu? '.format(c)))
    idade = date.today().year - n
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Há {} pessoa(s) maior(es) de idade.'.format(totmaior))
print('Há {} pessoa(s) menor(es) de idade.'.format(totmenor))