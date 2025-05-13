import time

class ContaBancaria:
    '''
    Classe que implementa métodos para manipular uma conta bancária.
    Atributos: titular (str), saldo (float), limite (float) e históricos (lista de dicionários) 

    OBS: Operações no histórico: 0 - Sacar, 1 - Depositar, 2 - Transferir
    '''

    def __init__(self, titular: str, saldo: float, limite: float, chaves_pix: list, historico: list) -> bool:
        '''
        Construtor da classe ContaBancaria
        '''
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__chaves_pix = chaves_pix
        self.__historico = historico

        return True
    
    def __str__(self) -> str:
        return f"Titular: {self.__titular}, Saldo: {self.__saldo}, Limite: {self.__limite}"
    
    def depositar(self, valor:float, remetente:str = None) -> bool:
        '''
        Objetivo: Método que realiza o depósito na conta bancária.

        Entrada: valor (float) remetente (str).

        Return: True, se a operação foi realizada com sucesso. False, se a operação não foi realizada. 

        '''
        operacao = 1
        # Detecta se é uma transferência
        if remetente != None:
            operacao = 2

        if valor > 0:
            self.__saldo += valor
            self.__historico.append({
                "operacao": operacao, 
                "remetente": remetente, 
                "destinatario": self.__titular, 
                "valor": valor, 
                "saldo": self.__saldo,
                "dataetempo": int(time.time())
            }) 

            return True
        else:
            print(f"O valor {valor} é inválido!")
            return False
        # Adicionar na lista de histórico
    
    def sacar(self, valor:float, destinatario:str = None) -> bool:
        '''
        Objetivo: Método que realiza o saque na conta bancária.

        Entrada: valor (float) destinatario (str).

        Return: True, se a operação foi realizada com sucesso. False, se a operação não foi realizada. 

        '''
        operacao = 0
        #Detecta se é uma transferência e altera a operação para 2
        if destinatario != None:
            operacao = 2

        if self.__saldo >= valor:
            self.__saldo -= valor
            self.__historico.append({
                "operacao": operacao, 
                "remetente": self.__titular, 
                "destinatario": destinatario, 
                "valor": valor, 
                "saldo": self.__saldo,
                "dataetempo": int(time.time())
            }) 
            return True
        else:
            a = input(f"Deseja utilizar o limite? (R$ {self.__limite}) [S para sim]")
            if a == "S":
                if (self.__saldo + self.__limite) >= valor:
                    self.__saldo -= valor
                    print("Saque Realizado!")

                    self.__historico.append({
                        "operacao": operacao, 
                        "remetente": self.__titular, 
                        "destinatario": destinatario, 
                        "valor": valor, 
                        "saldo": self.__saldo,
                        "dataetempo": int(time.time())
                    }) 
                    return True 
                else:
                    print("Saldo e limite insuficientes para realizar a operação!")
            else:
                print("Operação com limite cancelada!")
        return False
        # Adicionar na lista de histórico
    
    def transferir(self, valor: float, destinatario: str) -> bool:
        '''
        Objetivo: Método que realiza a transferência entre duas contas bancárias

        Entrada: valor (float), obj ContaBancaria do destinario (object)

        Return: Se ok -> True, Se NOK -> False. 

        '''
        # Se o saque ocorrer com sucesso
        if self.sacar(valor, destinatario.titular):
            # Deposita na conta do destinatário
            destinatario.depositar(valor, self.__titular)


    def exibir_historico(self) -> None:
        print(f"Histórico de transações de {self.__titular}:")
        for transacao in self.__historico:
            dt = time.localtime(transacao["dataetempo"])

            print("Operação:", transacao["operacao"], 
                  "| Remetente:", transacao["remetente"], 
                  "| Destinatário:", transacao["destinatario"], 
                  "| Valor:", transacao["valor"], 
                  "| Saldo:", transacao["saldo"], 
                  "| Data e tempo:", str(dt.tm_hour) + ":" + str(dt.tm_min) + ":" + str(dt.tm_sec) + " " + 
                  str(dt.tm_mday) + "/" + str(dt.tm_mon) + "/" + str(dt.tm_year))

    #def exibir_saldo(self) -> str:
    #    print(f"Saldo: {self.__saldo} Limite: {self.__limite}")        

    def getTitular(self) -> str:
        return self.__titular
    
    def getChavesPix(self) -> list:
        for chave in self.__chaves_pix:
            return chave

    
    
    
