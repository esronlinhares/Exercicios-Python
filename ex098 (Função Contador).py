from time import sleep

def contador(i, f, p):
    if p < 0:
       p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(0.3)
    if i < f:
        cont= i
        while cont <= f:
            print(cont, end=' ')
            sleep(0.3)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            sleep(0.3)
            cont -= p
        print('Fim!')
        
        
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)

'''from time import sleep

def contador():
    print('Contagem de 1 a 10 de 1 em 1')
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.3)
    print()
    print('Contagem de 10 a 0 de 2 em 2')
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(0.3)
    print()
    print('Agora é a sua vez de personalizar a contagem')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.3)
    
contador()'''
