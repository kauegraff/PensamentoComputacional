from utils.Erros import *

class ConversorMoeda:
    def __init__(self):
        self.__usd_to_brl = 5.05
        self.__eur_to_brl = 6.14
        self.__eur_to_usd = 1.22
    
    def converte_preco_para_usd(self, produto: object) -> bool:
        """
        Método que converte o preço de um produto para dólar

        Argumentos:

            produto (str): produto

        Retorno:

            True or False (bool): True se ok

        """
        try:
            if produto.getMoeda() == "BRL":
                produto.setMoeda("USD")
                # Calculo para alterar preço do produto de Reais para Dólar
                novo_preco = produto.getPreco() / self.__usd_to_brl
                produto.setPreco(novo_preco)
                return True
            elif produto.getMoeda() == "EUR":
                produto.setMoeda("USD")
                novo_preco = produto.getPreco() * self.__eur_to_usd
                produto.set_preco(novo_preco)
                return True
            elif produto.getMoeda() == "USD": 
                False
            else:
                raise MoedaInvalidErro("Moeda Inválida!")
    
        except MoedaInvalidErro as erro:
            print(f"Ocorreu o erro: {erro}")
    
    def converte_preco_para_eur(self, produto) -> bool:
        """
        Método que cálcula o consumo de combustível do veículo elétrico

        Argumentos:

            produto (str): produto

        Retorno:

            True or False (bool): True se ok

        """

        try:
            # Verifica o tipo da moeda
            if produto.getMoeda() == "BRL":
                # Altera o tipo da moeda
                produto.setMoeda("EUR")
                # Calculo para alterar o preço do produto
                novo_preco = produto.getPreco() / self.__eur_to_brl 
                # Altera o preço do produto
                produto.setPreco(novo_preco)
                return True
            elif produto.getMoeda() == "USD":
                produto.setMoeda("EUR")
                novo_preco = produto.getMoeda() / self.__eur_to_usd
                produto.setMoeda(novo_preco)
                return True
            elif produto.getMoeda() == "EUR":
                # Retorna falso caso o tipo da moeda já seja o desejado
                return False
            else: 
                # Trata uma possível exceção
                raise MoedaInvalidErro("Moeda Inválida")
            
        except MoedaInvalidErro as erro:
            print(f"Ocorreu o erro: {erro}")
    
    def converte_preco_para_brl(self, produto) -> bool:
        """
        Método que cálcula o consumo de combustível do veículo elétrico

        Argumentos:

            produto (str): produto

        Retorno:

            True or False (bool): True se ok

        """

        try:
            if produto.getMoeda() == "EUR":
                produto.setMoeda("BRL")
                novo_preco = produto.getPreco() * self.__eur_to_brl 
                produto.setPreco(novo_preco)
                return True
            elif produto.getMoeda() == "USD":
                produto.setMoeda("BRL")
                novo_preco = produto.getMoeda() * self.__usd_to_brl
                produto.setMoeda(novo_preco)
                return True
            elif produto.getMoeda() == "BRL":
                return False
            else: 
                raise MoedaInvalidErro("Moeda Inválida")
            
        except MoedaInvalidErro as erro:
            print(f"Ocorreu o erro: {erro}")


        

