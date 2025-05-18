class Veiculo:
    """
    Classe com as principais funcionalidades e atributos de um veículo, como modelo, marca, ano
    """
    def __init__(self, modelo:str, marca:str, ano:int, posicao: float) -> None:
        """
        Construtor do veículo
        """
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.posicao = posicao

    def __str__(self) -> str:
        """
        Retorna uma string com os principais atributos do objeto
        """
        info = f"Modelo: {self.__modelo}\n"
        info += f"Marca: {self.__marca}\n"
        info += f"Ano: {self.__ano}\n"
        info += f"Posição: {self.posicao}\n"
        return info

    def mover(self, distancia_percorrida: float) -> str:
        """
        Método que cálcula a nova posição do veículo em KM
        Argumentos:

            Distância percorrida (float): Distância percorrida

        Retorno:

            str: A nova posição do veículo
        """
        self.posicao += distancia_percorrida
        return f"O veículo está no KM {self.posicao}"


