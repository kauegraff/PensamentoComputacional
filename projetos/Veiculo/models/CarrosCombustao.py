from .Veiculos import Veiculos

class CarroCombustao(Veiculos):
    """
    Class que representa um carro a combustão, herda de Veiculos
    """
    def __init__(self, placa: str, modelo: str, cor: str, 
                    marca: str, ano: int, valor_fipe: float,
                    combustivel: str, nPortas: int, nAssentos: int,
                    nCilindradas: int, nCambio: str) -> None:
        super().__init__(placa, modelo, cor, 
                        marca, ano, valor_fipe) 
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindradas = nCilindradas
        self.__nCambio = nCambio

    def __str__(self) -> str:
        """
        Retorna uma string com as informações do carro de combustão
        """
        infos = super()__str__()
        # Adiciona as informações especificas do carro a combustão
        infos += f"Combustivel: {self.__combustivel}\n"
        infos += f"Número de portas: {self.__nPortas}\n"
        infos += f"Número de assentos: {self.__nAssentos}\n"
        infos += f"Número de cilindradas: {self.__nCilindradas}\n"
        infos += f"Câmbio: {self.__nCambio}\n"
        return infos