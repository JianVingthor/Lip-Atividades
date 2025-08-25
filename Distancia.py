'''Calcule a distância entre dois pontos 𝑝1(𝑥1, 𝑦1) e 𝑝2 𝑥2, 𝑦2 ,
mostrando o resultado com 4 casas decimais na tela:'''
import math
# jeito 1 de resolver 
#
coordenada_x1 = float(input("Informe a primeira cordenada do ponto p1: "))
coordenada_y1 = float(input("Informe a segunda cordenada do ponto p1: "))

coordenada_x2 = float(input("Informe a primeira cordenada do ponto p2: "))
coordenada_y2 = float(input("Informe a segunda cordenada do ponto p2: "))

distancia = math.sqrt((coordenada_x2 - coordenada_x1)**2 + (coordenada_y2 - coordenada_y1)**2)
print(f'distancia: {distancia}')