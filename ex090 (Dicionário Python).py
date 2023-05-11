aluno = {}
aluno['nome'] = str(input('Aluno: '))
aluno['media'] = float(input('Média: '))
for k, v in aluno.items():
    print(f'{k} é igual a {v}')