num = str(input("Digite um número de 0 a 9999: "))
dividido = num.split()
print('Unidade:', dividido[0][3])
print('Dezena:', dividido[0][2])
print('Centena:', dividido[0][1])
print('Milhar:', dividido[0][0])

#u = num // 1%10
#d = num // 10%10
#c = num // 100%10
#m = num // 1000%10
#print('Unidade: {}'.format(u))
#print('Dezena: {}'.format(d))
#print('Centena: {}'.format(c))
#print('Milhar: {}'.format(m))