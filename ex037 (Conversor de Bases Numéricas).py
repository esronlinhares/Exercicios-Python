num = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} em binário é {}.'.format(num, bin(num)))
elif opcao == 2:
    print('{} em octal é {}.'.format(num, oct(num)))
elif opcao == 3:
    print('{} em hexadecimal é {}.'.format(num, hex(num)))
else:
    print('Opção inválida.')