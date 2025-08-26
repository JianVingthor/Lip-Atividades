'''1) Calcule o rendimento médio do combustível em uma viagem. Mostre o resultado com três
casas decimais.'''

kilometros = float(input('Insira a quilometragem percorrido: '))
litros = float(input('Insira a litragem usada: '))

if(kilometros == 0) or (litros == 0):
    print('Ddos inconsistentes')
else:
    resultado = kilometros/litros

print(f'rendimento {resultado:.3f} Km/L')