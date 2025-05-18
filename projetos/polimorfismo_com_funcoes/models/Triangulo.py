class Triangulo:
    def __init__(self, altura:float, lado:float) -> None:
        """
        Método construtor da classe triangulo, leva em consideração um triangulo equilatero
        """
        self.altura = altura
        self.lado = lado
    
    def calcular_area(self) -> float:
        """
        Método que calcula a área do triangulo
        """
        area = self.lado * self.altura / 2
        return round(area, 2)