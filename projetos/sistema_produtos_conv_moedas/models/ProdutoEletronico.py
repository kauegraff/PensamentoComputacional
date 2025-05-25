from .Produto import Produto

class ProdutoEletronico(Produto):
    def __init__(self, nome: str, preco: float, moeda: str,  
                 voltagem: float, consumo_energia: float, sistema_op: str) -> None:
        """
        Construtor da classe produto alimenticio
        """
        super().__init__(nome, preco, moeda)
        self.__voltagem = voltagem
        self.__consumo_energia = consumo_energia
        self.__sistema_op = sistema_op

    def __str__(self) -> str:
        """ 
        Retorna as informações do produto alimenticio
        """ 
        info = super().__str__()
        info += f"Voltagem: {self.__voltagem}V \n"
        info += f"Consumo de Energia: {self.__consumo_energia}W \n"
        info += f"Sistema Operacional: {self.__sistema_op} \n"
        return info

