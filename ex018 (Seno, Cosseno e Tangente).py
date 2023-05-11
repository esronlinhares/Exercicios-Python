from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno de {} é: {:.2f}'.format(angulo, seno))
print('O cossenode de {} é {:.2f}'.format(angulo, cosseno))
print('A tangente de {} é {:.2f}'.format(angulo, tangente))
