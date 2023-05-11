def notas(*n, sit=False):
    """Analisar notas e situações de alunos.
        n: notas dos alunos.
        sit(opicional): Adicionar situação.
        return: dicionário com situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa.'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável.'
        else:
            r['situação'] = 'Ruim.'
    return r


print(notas(9, 10, 5.5, 2.5, 8.5, sit=True))
help(notas)
