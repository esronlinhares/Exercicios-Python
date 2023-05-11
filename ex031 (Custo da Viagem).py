km = float(input('Digite a distaância da viagem em km: '))
print('O preço da passagem é {}'.format(km*50) if km <=200 else 'O preço da passagem é {}'.format(km*45))