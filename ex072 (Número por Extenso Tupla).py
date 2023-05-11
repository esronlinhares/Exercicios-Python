n = ('zero', 'um', 'dois', 'três', 'quantro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
    'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
    'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    r = int(input('Digite um número entre 0 e 20: '))
    if 0 <= r <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número: {n[r]}.')