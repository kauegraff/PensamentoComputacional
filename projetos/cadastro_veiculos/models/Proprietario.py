import re

class Proprietario:
    def __init__(self, nome: str, cpf: str) -> None:
        """
        Construtor da classe Proprietario
        """
        self.__nome = nome
        self.__cpf = cpf 
        self.__placa = []

    def get_nome(self) -> None:
        return self.__nome
    
    def get_cpf(self) -> None:
        return self.__cpf

    def get_placas(self) -> None:
        return self.__placa
    
    def validar_cpf(self):
        cpf = re.sub(r'[^0-9]', '', self.__cpf)

        if len(cpf) != 11:
            return False
        elif cpf == cpf[0] * 11:
            return False
        else:
            return True
        

    def validar_placa(self, placa):
        if re.match(r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$', placa):
            return True
        else:
            return False

    def adicionar_veiculo(self, placa: str) -> None:
        self.__placa.append(placa)






