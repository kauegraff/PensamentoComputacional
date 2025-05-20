from .Veiculo import Veiculo

class VeiculoEletrico(Veiculo):
    """
    Classe Veiculo Eletrico
    """
    def __init__(self, placa: str, modelo: str, cor: str, 
                 marca: str, ano: int, valor_fipe: float) -> None:
        """
        Metodo construtor da classe veiculo eletrico
        """
        super().__init__(placa, modelo, cor, marca, ano, valor_fipe)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def calcular_consumo(self, distancia) -> float:
        """
        Método que cálcula o consumo de combustível do veículo elétrico

        Argumentos:

            distancia (float): distancia percorrida

        Retorno:

            calculo do consumo (float): calculo do consumo do veiculo elétrico em kWh

        """
        calculo = distancia / 0.15
        return calculo
    
    def recarregar(self) -> str:
        """
        Método que carrega o carro elétrico
        """
        return "Carro carregando..."