class Frota:
    def __init__(self, veiculo) -> None:
        """
        Método Construtor da classe Frota
        """
        self.__lista_veiculos = [veiculo]
    
    def adicionar_veiculo(self, veiculo) -> bool:
        """
        Método que adiciona véiculos na lista de veículos

        Argumentos: 
            veiculo (obj): objeto com o veículo

        Retorno:
            True se ok    
        """
        self.__lista_veiculos.append(veiculo)
        return True
    
    def exibir_frota(self) -> str:
        """
        Metodo que exibi a frota de veículos presentes na lista
        """
        for frota in self.__lista_veiculos:
            print(frota)
    
    def calcular_consumo(self, distancia):
        """
              Método que cálcula o consumo de 
              combustível da frota de veiculos

        Argumentos:

            distancia (float): distancia percorrida

        Retorno:

            calculo do consumo (float): calculo do consumo da frota

        """
        soma = 0
        for veiculo in self.__lista_veiculos:
            soma += veiculo.calcular_consumo(distancia)
        return soma