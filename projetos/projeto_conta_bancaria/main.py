from models.ContaBancaria import ContaBancaria

conta1 = ContaBancaria('Kauê', 1300, 1200, [])
conta2 = ContaBancaria('Jose', 2000, 1500, [])

conta1.depositar(150)
conta1.exibir_historico()
conta1.sacar(100)
conta1.exibir_historico()
conta1.transferir(1000, conta2)
conta1.exibir_historico()
conta2.exibir_historico()

