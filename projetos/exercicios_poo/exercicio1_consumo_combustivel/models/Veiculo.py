import re

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
    
    def validar_placa(placa:str) -> bool:
        if len(placa) == 7:
            return re.match(r"^[A-Z]{3}\d{4}$", placa)

    def calcular_consumo(self, distancia: float) -> str:
        """
        Método que cálcula o consumo de combustível do veículo

        Argumentos:

            distancia (float): distancia percorrida

        Retorno:

            string (str): Aguarda uma subclasse para realizar o cálculo

        """
        return f"Metodo somento disponivel para subclasses"
    
    def getModelo(self) -> str:
        """
        Método que mostra o modelo do veiculo
        """
        return self.__modelo

    def getPlaca(self) -> str:
        return self.__placa
    
    def setPlaca(self, nova_placa) -> str:
        if re.match(r"^[A-Z]{3}\d{4}$", nova_placa):
            self.__placa = nova_placa
        else:
            print("Placa Inválida!")


    def __eq__(self, other) -> bool:
        """
        Método que verifica se um atributo de um objeto é igual ao outro
        Argumentos:
            other (obj): o outro objeto que vai ser comparado
        """
        if isinstance(other, Veiculo):
            return self.__placa == other.getPlaca()
        else:
            return False

             
        
    
