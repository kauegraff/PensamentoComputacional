from models.Retangulo import Retangulo
from models.Triangulo import Triangulo

def exibir_area(figura):
    print(f"A área é: {figura.calcular_area()}")

retangulo = Retangulo(3.5, 2.1)
triangulo = Triangulo(2, 3)

exibir_area(retangulo)
exibir_area(triangulo)