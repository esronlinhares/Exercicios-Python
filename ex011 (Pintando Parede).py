largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura*altura
tinta = area/2
print('Será necessário {:.1f} litros de tinta para pintar uma área de {:.2f} m²'.format(tinta, area))