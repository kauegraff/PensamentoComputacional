from models.ContaBancaria import ContaBancaria

conta1 = ContaBancaria('Kauê', 1349.40, 1200)
conta2 = ContaBancaria('Eduarda', 0, 4000)

print("Conta Bancária")

# Tela Login -> Login ou Cadastro

opcao = input("""\n Qual operação você deseja realizar: \n
    1 - Depositar
    2 - Sacar 
    3 - Transferir
""")

if opcao == "1":
    valor = float(input("Digite o valor que você deseja depositar: "))
    conta1.depositar(valor)
elif opcao == "2":
    valor = float(input("Digite o valor que você deseja sacar: "))
    conta1.sacar(valor)
elif opcao == "3":
    valor = float(input("Digite o valor que você deseja transferir: "))
    conta1.transferir(valor, conta2)
else:
    print("Opção digitada inválida")



"""conta1.exibir_saldo()
conta1.depositar(10000)
conta1.exibir_saldo()
conta1.sacar(2000)
conta1.exibir_saldo()

conta1.transferir(1000, conta2)

conta1.exibir_saldo()
conta1.exibir_historico()
conta2.exibir_historico()
conta2.exibir_saldo()
conta2.exibir_saldo()"""

conta1.exibir_saldo()
conta1.exibir_historico()
conta2.exibir_saldo()
conta2.exibir_historico()

