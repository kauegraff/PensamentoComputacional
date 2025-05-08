from models.ContaBancaria import ContaBancaria

'''conta1 = ContaBancaria('Kauê', 1300, 1200, [])
conta2 = ContaBancaria('Jose', 2000, 1500, [])'''

#- 1: criar conta;
#- 3: sacar
#- 4: depositar
#- 3 realizar transferência
#- 2: excluir conta (solicitar conta para transferir o saldo restante, ou depositar o que falta para zerar a conta)
lista_contas = []

r = "s"


# Busca as contas na lista
def buscar_conta(lista_contas, titular):
    for conta in lista_contas:
        if conta.titular == titular:
            return True
    else:
        return False


while r == "s":
    operacao = input("Digite:\n 1 - Criar Uma Conta | \n 2 - Sacar  |\n 3 - Depositar |\n 4 - Realizar uma transferência |\n 5 - Excluir Conta | \n 6 - Exibir Saldo | \n 7 - Exibir Extrato \n")
    if operacao == "1":
        # Criar função
        print("*** CADASTRO ***")
        print("Complete o formulário abaixo para criar a sua conta:")
        # Criar verificação para o nome do usuário
        titular_procurado = input("Digite o nome do titular: ")
        saldo = input("Digite o saldo da conta: ")
        limite = input("Digite o limite da conta: ")
        lista_contas.append(ContaBancaria(titular_procurado, saldo, limite, []))

    elif operacao == "2":
        # Verificar se o titular existe
        titular_procurado = input("Digite de qual conta será sacado o valor: ")
        # Verificar se o valor sacado é um número (float)
        if buscar_conta(lista_contas, titular_procurado):
            valor_sacado = input("Digite o valor que será sacado: ")
            conta.sacar(valor_sacado)
            print("Valor sacado")

    
    elif operacao == "3":
        titular_procurado = titular_procurado = input("Digite de qual conta será sacado o valor: ")
        for conta in lista_contas:
            if conta.titular == titular_procurado:
                valor_deposito = input("Digite o valor a ser depositado: ")
                conta.depositar(valor_deposito)
        else:
            print("Titular não encontrado!")
    
    elif operacao == "4":
        titular_procurado = input("Digite o titular da conta que fará a tranferência")
        for conta in lista_contas:
            if conta.titular == titular_procurado:
                destinatario = input("Digite o nome do titular da conta destinataria: ")
                for dest in lista_contas:
                    if destinatario == dest:
                        valor_transferido = input("Digite o valor que será transferido: ")
                        conta.transferir(valor_transferido, dest)
                        print("Valor Transferido")
                else:
                    print("Destinatario não encotrado!")

    elif operacao == "5":
        titular_procurado = input("Digite o titular da conta que você deseja excluir: ")
        for conta in lista_contas:
            if conta.titular == titular_procurado:
                index_remove = lista_contas.index(conta)
                del lista_contas[index_remove]
                print("Conta removida da lista")

    elif operacao == "6":
        titular_procurado = input("Digite o titular da conta que deseja ver o saldo: ")
        for conta in lista_contas:
            if conta.titular == titular_procurado:
                conta.exibir_saldo()
    
    r = input("Deseja continuar? [s, n]")



