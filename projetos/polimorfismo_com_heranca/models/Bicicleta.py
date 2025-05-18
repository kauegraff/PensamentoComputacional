from .Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, modelo: str, marca: str, ano: int, posicao: float,
                tamanho_quadro: int, aro: float, qtd_marchas: int) -> None:
        """
        Método construtor da classe Bicicleta
        """
        super().__init__(modelo, marca, ano, posicao)
        self.__tamanho_quadro = tamanho_quadro
        self.__aro = aro
        self.__qtd_marchas = qtd_marchas

    def __str__(self) -> str:
        """
        Método que retorna uma string com os atributos da classe bicicleta
        """
        info = super().__str__()
        info = f"Tamanho do Quadro: {self.__tamanho_quadro}\n"
        info += f"Aro: {self.__aro}\n"
        info += f"Quantidade de Marchas: {self.__qtd_marchas}\n"
        return info
    
    def mover(self, distancia_percorrida: float) -> str:
        """
        Método que cálcula a nova posição da bicleta em KM
        Argumentos:

            Distância percorrida (float): Distância percorrida em KM

        Retorno:

            str: A nova posição da Bicicleta
        """
        self.posicao += distancia_percorrida
        return f"A bicicleta está no KM {self.posicao}"
