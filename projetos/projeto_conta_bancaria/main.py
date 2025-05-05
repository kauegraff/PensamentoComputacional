from models.ContaBancaria import ContaBancaria

conta1 = ContaBancaria('Kauê', 1349.40, 1200, 0)
conta2 = ContaBancaria('Eduarda', 0, 4000, 0)
conta1.exibir_saldo()
conta1.depositar(10000)
conta1.exibir_saldo()
conta1.sacar(2000)
conta1.exibir_saldo()

conta1.transferir(1000, conta2)

conta1.exibir_saldo()
conta1.exibir_historico()
conta2.exibir_historico()
conta2.exibir_saldo()
conta2.exibir_saldo()

