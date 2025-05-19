from .Veiculo import Veiculo

class Frota():
    def __init__(self, lista_veiculos: list) -> None:
        """
        Método Construtor da classe Frota
        """
        self.__lista_veiculos = []
    
    def adicionar_veiculo(self, veiculo) -> bool:
        self.__lista_veiculos.append(Veiculo)
        return True
    
    def exibir_frota(self):
        for frota in self.__lista_veiculos:
            print(frota)
    
    def getFrota(self):
        return self.__lista_veiculos