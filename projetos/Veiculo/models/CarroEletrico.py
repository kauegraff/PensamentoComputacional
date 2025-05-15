from .Veiculos import Veiculos

class CarroEletrico(Veiculos):
    """
    Classe que implementa métodos especificos de carros elétricos
    Argumento: Classe pai Veiculo
    """
    def __init__(self, placa: str, modelo: str, cor: str, marca: str, ano: int, valor_fipe: float,
                        nAssentos: int, nPortas: int, nivel_bateria: int, tipo_bateria: str, 
                        autonomia: int):
        Veiculos.__init__(self, placa, modelo, cor, marca, ano, valor_fipe)
        self.__nAssentos = nAssentos
        self.__nPortas = nPortas
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia 

    def __str__(self):
        infos = super().__str__()
        infos += f"Número de portas: {self.__nPortas}\n"
        infos += f"Número de assentos: {self.__nAssentos}\n"
        infos += f"Nível da Bateria: {self.__nivel_bateria}\n"
        infos += f"Tipo da Bateria: {self.__tipo_bateria}\n"
        infos += f"Autonomia: {self.__autonomia}\n"
        return infos

    def get_nivel_bateria(self):
        return self.__nivel_bateria
    
    def get_tipo_bateria(self):
        return self.__tipo_bateria
    
    def get_autonomia(self):
        return self.__autonomia