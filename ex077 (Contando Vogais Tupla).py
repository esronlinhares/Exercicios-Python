t = ('amor', 'discoteca', 'esron', 'tupla')
for p in t:
    print(f'\nNa palavra {p} temos ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')