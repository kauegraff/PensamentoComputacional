from .Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, placa: str, modelo:str, cor:str, marca:str, ano:int, valor_fipe:float) -> None:
        """
        Método construtor da classe moto
        """
        super().__init__(placa, modelo, cor, marca, ano, valor_fipe)
    
    def __str__(self):
        """
        Método que imprime os atributos básicos da classe
        """
        return super().__str__()
    
    def calcular_consumo(self, distancia) -> float:
        """
        Método que cálcula o consumo de combustível da moto

        Argumentos:

            distancia (float): distancia percorrida

        Retorno:

            calculo do consumo (float): calculo do consumo da moto 

        """

        calculo_consumo = distancia / 20
        return calculo_consumo


