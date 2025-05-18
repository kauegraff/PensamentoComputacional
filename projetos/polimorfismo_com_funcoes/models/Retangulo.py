class Retangulo:    
    def __init__(self, lado1: float, lado2: float) -> None:
        """
        Método construtor do retangulo
        """
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self) -> float:
        """
        Método que calcula a área do retangulo
        """
        area = self.lado1 * self.lado2
        return round(area, 2)

        