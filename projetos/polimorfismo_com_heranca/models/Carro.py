from .Veiculo import Veiculo

class Carro(Veiculo):
    """
    Classe que herda os atributos de veículo e cria atributos especifico para si
    """
    def __init__(self, modelo: str, marca: str, ano: int, posicao: float, 
                 combustivel: str, potencia:int, cilindros: int) -> None:
        """
        Método construtor do Carro
        """
        super().__init__(modelo, marca, ano, posicao)
        self.__combustivel = combustivel
        self.__potencia = potencia
        self.__cilindros = cilindros
    
    def __str__(self):
        info = super().__str__()
        info += f"Combustivel: {self.__combustivel}\n"
        info += f"Potência: {self.__potencia} CV\n"
        info += f"Quantidade de Cilindros; {self.__cilindros} \n"

    def mover(self, distancia_percorrida: float) -> str:
        """
        Método que cálcula a nova posição do carro em KM
        Argumentos:

            Distância percorrida (float): Distância percorrida

        Retorno:

            str: A nova posição do carro
        """
        self.posicao += distancia_percorrida
        return f"O carro está no KM {self.posicao}"