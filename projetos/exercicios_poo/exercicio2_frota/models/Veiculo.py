class Veiculo:
    """ 
    Classe com as pincipais funcionalidades do sistema de veículos, como placa, modelo, cor, valor da fipe
    """

    def __init__(self, placa: str, modelo: str, cor: str, 
                    marca: str, ano: int, valor_fipe: float) -> None:
        """Construtor da classe Veiculos"""
        self.__placa = placa
        self.__modelo = modelo
        self.__cor = cor
        self.__marca = marca
        self.__ano = ano
        self.__valor_fipe = valor_fipe
    
    def __str__(self) -> str:
        """Retorna uma string com as informações do veiculo"""
        infos = f"Placa: {self.__placa}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Valor da fipe: {self.__valor_fipe}\n"
        return infos
    
    def calcular_consumo(self, distancia: float) -> str:
        """
        Método que cálcula o consumo de combustível do carro
        """
        calculo_consumo = distancia
        return f"O consumo do carro foi de {round(calculo_consumo, 2)} litros"


