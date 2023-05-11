frase = (str(input("Escreva uma frase: "))).lower().strip()
print('Existem {} letras A na frase'.format(frase.count('a')))
print('Aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
print('Aparece pela úiltima vez na posição {}'.format(frase.rfind('a')+1))