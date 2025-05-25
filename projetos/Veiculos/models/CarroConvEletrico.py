from .CarrosCombustao import CarroCombustao
from .CarroEletrico import CarroEletrico

class CarroConvEletrico(CarroCombustao, CarroEletrico):
    """
    Classe que implementa métodos especificos de um carro convertido 
    em elétrico
    """

    def __init__(self, placa: str, modelo: str, cor: str, 
                    marca: str, ano: int, valor_fipe: float,
                    combustivel: str, nPortas: int, nAssentos: int,
                    nCilindradas: int, nCambio: str, nivel_combustivel: int,
                    nivel_bateria: int, tipo_bateria: str, autonomia: int) -> None:
        
        CarroCombustao.__init__(self, placa, modelo, cor, marca, ano, valor_fipe, 
                         combustivel, nPortas, nAssentos, nCilindradas, nCambio, nivel_combustivel)
        
        CarroEletrico.__init__(self, placa, modelo, cor, marca, ano, valor_fipe, nAssentos, nPortas, 
                               nivel_bateria, tipo_bateria, autonomia)
    
    def __str__(self) -> str:
        infos = CarroCombustao.__str__(self)
        infos += f"Nível da Bateria: {CarroEletrico.get_nivel_bateria(self)}\n"
        infos += f"Tipo da Bateria: {CarroEletrico.get_tipo_bateria(self)}\n"
        infos += f"Autonomia: {CarroEletrico.get_autonomia(self)}\n"
        return infos
    
    def abastecer(self, percentual_adicionado) -> bool:
        """Método abastecer desativado

        Args:

            percentual_adicionado

        Returns:

            False, pois não pode abastecer

        """
        print("Carro convertifdo para Elétrico! Não é mais possível abastecer!")
        return False

        