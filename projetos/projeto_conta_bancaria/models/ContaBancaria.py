class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = [] 
        self.id_historico = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.id_historico += 1
            self.salvar_historico("Deposito", valor, " ")
            """self.historico.append({
                "valor": valor, 
                "titular_conta": self.titular, 
                "tipo_transacao": "Deposito", 
                "id_transacao": self.id_historico, 
                "natureza": " "
            })"""
        else:
            print(f"O valor {valor} é inválido!")
        # Adicionar na lista de histórico
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.id_historico += 1
            self.historico.append({
                "valor": valor, 
                "titular_conta": self.titular, 
                "tipo_transacao": "Sacar", 
                "id_transacao": self.id_historico, 
                "natureza": "Saldo"
            }) 
        else:
            a = input(f"Deseja utilizar o limite? (R$ {self.limite}) [S para sim]")
            if a == "S":
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print("Saque Realizado!")

                    self.id_historico += 1
                    self.historico.append({
                    "valor": valor, 
                    "titular_conta": self.titular, 
                    "tipo_transacao": "Saque", 
                    "id_transacao": self.id_historico, 
                    "natureza": "Limite"
                    })    
                else:
                    print("Saldo e limite insuficientes para realizar a operação!")
            else:
                print("Operação com limite cancelada!")
        # Adicionar na lista de histórico
    
    def transferir(self, valor, conta_destino):
        if self.saldo > valor:
            self.saldo -= valor
            self.id_historico += 1
            self.historico.append({
                "valor": valor, 
                "titular_conta": self.titular, 
                "tipo_transacao": "Transferência Enviada", 
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
    
    def salvar_historico(conta, tipo_transacao, valor, natureza):
        if tipo_transacao == "Deposito":
            conta.historico.append({
                "valor": valor, 
                "titular_conta": conta.titular, 
                "tipo_transacao": "Deposito", 
                "id_transacao": conta.id_historico, 
                "natureza": " "
        })
        elif tipo_transacao == "Sacar":
            if natureza == "Saldo":
                conta.historico.append({
                    "valor": valor, 
                    "titular_conta": conta.titular, 
                    "tipo_transacao": "Sacar", 
                    "id_transacao": conta.id_historico, 
                    "natureza": "Saldo"
                })
            elif natureza == "Limite":
                conta.historico.append({
                    "valor": valor, 
                    "titular_conta": conta.titular, 
                    "tipo_transacao": "Sacar", 
                    "id_transacao": conta.id_historico, 
                    "natureza": "Limite"
                })
            else: 
                print("Natureza inválida!")
        elif tipo_transacao == "Transferencia":
            pass

