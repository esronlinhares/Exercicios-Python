from random import randint
n1 = randint(0, 10)
n2 = p = 0
#acertou = False
#while not acertou:
while n1 != n2:
    n2 = int(input('Adivinhe um número de 0 a 10: '))
    p += 1
    if n2 > n1:
        print('O número correto é menor que {}'.format(n2))
    if n2 < n1:
        print('O número correto é maior que {}'.format(n2))
    if n1 == n2:
        print('Você acertou com {} palpites.'.format(p))
        #acertou = True 