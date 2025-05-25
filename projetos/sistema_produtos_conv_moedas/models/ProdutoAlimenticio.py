from .Produto import Produto

class ProdutoAlimenticio(Produto):
    def __init__(self, nome: str, preco: float, moeda: str,  
                 carboidratos: float, proteinas: float, gorduras_tot: float) -> None:
        """
        Construtor da classe produto alimenticio
        """
        super().__init__(nome, preco, moeda)
        self.__carboidratos = carboidratos
        self.__proteinas = proteinas
        self.__gorduras_tot = gorduras_tot

    def __str__(self) -> str:
        """
        Retorna as informações do produto alimenticio
        """
        info = super().__str__()
        info += f"Carboidratos: {self.__carboidratos}g \n"
        info += f"Proteinas: {self.__proteinas}g \n"
        info += f"Gorduras Totais: {self.__gorduras_tot}g \n"
        return info


