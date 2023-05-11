from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto oposto: '))
h = hypot(co, ca)
print('O valor da ipotenusa é {:.2}: '.format(h))