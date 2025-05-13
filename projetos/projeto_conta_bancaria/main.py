from models.ContaBancaria import ContaBancaria

lista_contas = []

r = "s"

# Busca as contas na lista de contas
def buscar_conta(lista_contas):
    # Entrada do titular que será procurado na lisa
    titular = input("Digite o titular da conta: ")
    # Percorre a lista de contas
    for conta in lista_contas:
        if conta.getTitular() == titular:
            return conta # Quando a conta for encontrada retorna a conta
    return None # Se a conta não for encontrada retorna None/Nada

# Verifica se uma conta já existe dentro da lista de contas
def verificar_duplicidade(conta_procurada, lista_contas):
    # Percorre a lista de contas
    for conta in lista_contas:
        if conta.getTitular() == conta_procurada:
            return True # Se conta já existe retorna Verdadeiro 
        return False # Se a conta não for encontrada retorna falso

while r == "s":
    operacao = input(
"""
Digite:\n 
[1] - Criar Uma Conta | 
[2] - Sacar  |
[3] - Depositar |
[4] - Realizar uma transferência |
[5] - Excluir Conta |  
[6] - Exibir Saldo |  
[7] - Exibir Histórico 
[8] - Realizar PIX
""")
    
    if operacao == "1":
        print("*** CADASTRO ***")
        print("Complete o formulário abaixo para criar a sua conta!")
        # Entrada para o nome do titular da conta
        titular = input("Digite o nome do titular: ")
        # Verifica se a conta já existe na lista
        if verificar_duplicidade(titular, lista_contas): 
            print("Essa conta já existe! Voltando ao menu principal...")
            continue
        saldo = float(input("Digite o saldo da conta: "))
        limite = float(input("Digite o limite da conta: "))
        chave_pix_1 = input("Cadastrar Chave Pix I: ")
        chave_pix_2 = input("Cadastrar Chave Pix II: ")
        chave_pix_3 = input("Cadastrar Chave Pix III: ")

        # Salva as entradas do usuário na lista
        lista_contas.append(ContaBancaria(titular, saldo, limite, [chave_pix_1, chave_pix_2, chave_pix_3], []))
   
    elif operacao == "2":
        print("*** SAQUE ***")
        conta = buscar_conta(lista_contas)
        # Se a conta estiver na lista faz a operação de saque
        if conta:
            valor_sacado = float(input("Digite o valor que será sacado: "))
            conta.sacar(valor_sacado)
            print(f"Valor R${valor_sacado} sacado!")
        else: 
            print("Titular não encontrado!")
    
    elif operacao == "3":
        print("*** DEPÓSITO ***")
        conta = buscar_conta(lista_contas)
        # Verifica se a conta existe para realizar a operacao
        if conta:
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor_deposito)
            print(f"Valor de {valor_deposito} depositado com sucesso!")
        else:
            print("Titular não encontrado!")
    
    elif operacao == "4":
        print("*** TRANSFERÊNCIA ***")
        print("- REMETENTE -")
        conta_remetente = buscar_conta(lista_contas)
         # Verifica se a conta existe para realizar a operacao
        if conta_remetente:
            print("- DESTINATARIO -")
            conta_destino = buscar_conta(lista_contas)
             # Verifica se a conta existe para realizar a operacao
            if conta_destino:
                valor_transferido = float(input(f"Digite o valor que será transferido para {conta_destino.titular}: "))
                conta_remetente.transferir(valor_transferido, conta_destino)
                print(f"Valor R${valor_transferido} Transferido Para {conta_destino.titular}")
            else: 
                print("Titular não encontrado!")
        else:
            print("Titular não encontrado!")

    elif operacao == "5":
        print("*** REMOVER CONTA ***")
        print("CONTA QUE SERÁ REMOVIDA")
        conta = buscar_conta(lista_contas)
         # Verifica se a conta existe para realizar a operacao
        if conta:
            # Verifica se há saldo na conta que será exluida e transfere o saldo para outra conta
            if conta.saldo > 0:
                print("CONTA QUE SERÁ ENVIADA O RESTANTE DO SALDO")
                conta_destino = buscar_conta(lista_contas)
                if conta_destino:
                    saldo = conta_destino.saldo
                    conta.transferir(saldo, conta_destino)
                else: 
                    print("Titular da conta de destino não encontrado!")
                    continue
            # Procura o indice da conta na lista
            index_remove = lista_contas.index(conta)
            # Deleta a conta da lista
            del lista_contas[index_remove]
            print("Conta removida da lista")
        else:
            print("Titular não encontrado!")

    elif operacao == "6":
        print("*** EXIBIR SALDO ***")
        conta = buscar_conta(lista_contas)
        if conta:
            print(conta)
        else: 
            print("Titular não encontrado!")
    
    elif operacao == "7":
        print("*** EXIBIR HISTORICO ***")
        conta = buscar_conta(lista_contas)
        if conta: 
            conta.exibir_historico()
        else:
            print("Titular não encontrado!")
    elif operacao == "8":
        print("*** PIX ***")
        conta = buscar_conta(conta)
        if conta:
            pass
        else:
            print("Titular não encontrado")
        chave_pix = input("Digite a chave pix: ")
        if chave_pix in conta.getChavesPix:
            pass
    
    r = input("Deseja continuar? [s, n]")

