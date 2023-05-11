from random import randint

def sorteia(l):
    for c in range(0, 5):
        n = randint(1, 5)
        l.append(n)
        print(n, end=' ')
        
        
def somaPar(l):
    s = 0
    for v in l:
        if v % 2 == 0:
            s += v
    print(f'A soma dos valores pares de {l} é {s}.')
    
    
numeros = []
sorteia(numeros)
print()
somaPar(numeros)
