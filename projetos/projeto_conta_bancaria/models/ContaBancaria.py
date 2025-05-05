class ContaBancaria:
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = [] 
        self.id_historico = 0
    
    def depositar(self, valor):
        self.saldo += valor
        self.id_historico += 1
        self.historico.append({
            "valor": valor, 
            "titular_conta": self.titular, 
            "tipo_transacao": "Deposito", 
            "id_transacao": self.id_historico, 
            "natureza": " "})
        # Adicionar na lista de histórico
    
    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            self.id_historico += 1
            self.historico.append({"valor": valor, "titular_conta": self.titular, 
                                "tipo_transacao": "Deposito", "id_transacao": self.id_historico, "natureza": "Saldo"})  
        elif self.limite > valor:
            self.limite -= valor
            self.id_historico += 1
            self.historico.append({"valor": valor, "titular_conta": self.titular, 
                                "tipo_transacao": "Deposito", "id_transacao": self.id_historico, "natureza": "Limite"}) 
        else:
            print("Saldo e limite insuficientes para realizar a operação!")
        # Adicionar na lista de histórico
    
    def transferir(self, valor, conta_destino):
        if self.saldo > valor:
            self.saldo -= valor
            self.id_historico += 1
            self.historico.append({
                "valor": valor, 
                "titular_conta": self.titular, 
                "tipo_transacao": "Transferência", 
                "id_transacao": self.id_historico, 
                "natureza": "Saldo"
            })
            conta_destino.saldo += valor
            conta_destino.id_historico += 1
            conta_destino.historico.append({
                "valor": valor, 
                "titular_conta": conta_destino.titular, 
                "tipo_transacao": "Transferência Recebida", 
                "id_transacao": conta_destino.id_historico, 
                "natureza": "Saldo"
            })
        else:
            print("Saldo insuficiente para realizar a operação!")

    def exibir_historico(self):
        print(self.historico)

    def exibir_saldo(self):
        print(f"Saldo: {self.saldo} Limite: {self.limite}")