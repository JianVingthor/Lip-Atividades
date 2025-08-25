'''Dados o peso e a altura de uma pessoa, calcule e exiba seu IMC
mostrando apenas 2 casas decimais:'''
peso = float(input("Coloque seu peso aqui: "))
altura = float(input("Coloque sua altura aqui: "))
resultado = peso/(altura*altura)

print(f'IMC: {resultado:.2f}')