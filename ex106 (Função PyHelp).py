def ajuda(com):
    titulo(f'Acessando o manual do comando {com}')
    help(com)
def titulo(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)