def fatorial(n, show=False):
    """Calcula o fatorial de um número.
        n: o número a ser calculado.
        show (opcional): Mostrar a conta.
        return: o valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
print(fatorial(5))
print(fatorial(5, show=True))
help(fatorial)