from random import randint

n1 = randint (0,5)
n2 = int(input('Adivinhe um número de 0 a 5: '))
print('Você acertou!' if n1 == n2 else 'Você errou!')
print('O número correto é {}'.format(n1))