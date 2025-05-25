class Produto:
    def __init__(self, nome: str, preco: float, moeda: str) -> None:
        """
        Construtor da classe produto
        """
        self.__nome = nome
        self.__preco = preco
        self.__moeda = moeda
    
    def __str__(self) -> str:
        """
        Retorna as informações do produto
        """
        info = f"Produto: {self.__nome}\n"
        info += f"Preço: {self.__preco}\n"
        info += f"Moeda: {self.__moeda}\n"
        return info
    
    def getNome(self) -> str:
        """
        Método que retorna o atributo privado nome
        """
        return self.__nome

    def getPreco(self) -> str:
        """
        Método que retorna o atributo privado preço
        """
        return self.__preco
    
    def getMoeda(self) -> str:
        """
        Método que retorna o atributo privado preço
        """
        return self.__moeda 
    
    def setNome(self, novo_nome):
        """
        Método que altera o nome do produto

        Argumentos: novo nome (str): Defini o novo nome do prodto

        Retorno: True se ok (bool)
        """
        self.__nome = novo_nome 
        return True
    
    def setPreco(self, novo_preco):
        """
        Método que altera o preço do produto
        
        Argumentos: Novo preço (float): Defini o novo preço do produto

        Retorno: True se ok (bool)
        """
        self.__preco = novo_preco
        return True
    
    def setMoeda(self, nova_moeda):
        """
        Método que altera a moeda
        
        Argumentos: Nova moeda (str): Defini a nova moeda do produto

        Retorno: True se ok (bool)
        """
        self.__moeda = nova_moeda
        return True
    