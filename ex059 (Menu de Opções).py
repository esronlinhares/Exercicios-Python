n1 = int(input('Insira o 1º valor: '))
n2 = int(input('Insira o 2º valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Qual sua opção? '''))
    if opcao == 1:
        print('A soma dos valores é: {}.'.format(n1+n2))
    if opcao == 2:
        print('A multiplicação dos valores é: {}'.format(n1*n2))
    if opcao == 3:
        if n1 > n2:
            print('{} é o número maior.'.format(n1))
        if n1 < n2:
            print('{} é o número maior.'.format(n2))
        if n1 == n2:
            print('Os dois valores são iguais.')
    if opcao == 4:
        n1 = int(input('Insira o 1º valor: '))
        n2 = int(input('Insira o 2º valor: '))
    if opcao == 5:
        print('Finalizando.')
    else:
        print('Opção inválida. Tente novamente')