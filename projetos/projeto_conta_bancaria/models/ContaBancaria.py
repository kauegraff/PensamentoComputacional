import time

class ContaBancaria:
    '''
    Classe que implementa métodos para manipular uma conta bancária.
    Atributos: titular (str), saldo (float), limite (float) e históricos (lista de dicionários) 

    OBS: Operações no histórico: 0 - Sacar, 1 - Depositar, 2 - Transferir
    '''

    def __init__(self, titular, saldo, limite, historico):
        '''
        Construtor da classe ContaBancaria
        '''
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = [] 
        self.id_historico = 0
    
    def depositar(self, valor):
        '''
        Objetivo: Método que realiza o depósito na conta bancária.

        Entrada: valor (float)

        Return: True, se a operação foi realizada com sucesso. False, se a operação não foi realizada. 

        '''
        if valor > 0:
            self.saldo += valor
            self.historico.append({
                "operacao": 1, 
                "remetente": self.titular, 
                "destinatario": None, 
                "valor": valor, 
                "saldo": self.saldo,
                "dataetempo": int(time.time())
            }) 

            return True
        else:
            print(f"O valor {valor} é inválido!")
            return False
        # Adicionar na lista de histórico
    
    def sacar(self, valor):
        '''
        Objetivo: Método que realiza o saque na conta bancária.

        Entrada: valor (float)

        Return: True, se a operação foi realizada com sucesso. False, se a operação não foi realizada. 

        '''

        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.append({
                "operacao": 0, 
                "remetente": self.titular, 
                "destinatario": None, 
                "valor": valor, 
                "saldo": self.saldo,
                "dataetempo": int(time.time())
            }) 
            return True
        else:
            a = input(f"Deseja utilizar o limite? (R$ {self.limite}) [S para sim]")
            if a == "S":
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print("Saque Realizado!")

                    self.historico.append({
                        "operacao": 0, 
                        "remetente": self.titular, 
                        "destinatario": None, 
                        "valor": valor, 
                        "saldo": self.saldo,
                        "dataetempo": int(time.time())
                    }) 
                    return True 
                else:
                    print("Saldo e limite insuficientes para realizar a operação!")
            else:
                print("Operação com limite cancelada!")
        return False
        # Adicionar na lista de histórico
    
    def transferir(self, valor, conta_destino):
        if self.saldo > valor:
            self.saldo -= valor
            self.historico.append({
                "operacao": 2, 
                "remetente": self.titular, 
                "destinatario": conta_destino.titular, 
                "valor": valor, 
                "saldo": self.saldo,
                "dataetempo": int(time.time())
            }) 
            conta_destino.saldo += valor
            conta_destino.historico.append({
                "operacao": 2, 
                "remetente": self.titular, 
                "destinatario": conta_destino.titular, 
                "valor": valor, 
                "saldo": conta_destino.saldo,
                "dataetempo": int(time.time())
            })

        else:
            print("Saldo insuficiente para realizar a operação!")

    def exibir_historico(self):
        print(f"Histórico de transações de {self.titular}:")
        for transacao in self.historico:
            dt = time.localtime(transacao["dataetempo"])

            print("Operação:", transacao["operacao"], 
                  "| Remetente:", transacao["remetente"], 
                  "| Destinatário:", transacao["destinatario"], 
                  "| Valor:", transacao["valor"], 
                  "| Saldo:", transacao["saldo"], 
                  "| Data e tempo:", str(dt.tm_hour) + ":" + str(dt.tm_min) + ":" + str(dt.tm_sec) + " " + 
                  str(dt.tm_mday) + "/" + str(dt.tm_mon) + "/" + str(dt.tm_year))

    def exibir_saldo(self):
        print(f"Saldo: {self.saldo} Limite: {self.limite}")
    
