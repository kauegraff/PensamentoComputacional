from models.Veiculos import Veiculos


gol = Veiculos("Gol Copa", "Volkswagen", 2006, "Amarelo", 0, "IND-1010", 
               0, 0)

gol.exibirInfos()
gol.acelerar()
gol.exibirInfos()
gol.desacelerar()
gol.exibirInfos()

gol.alterarPlaca("IND1A10")
gol.exibirInfos()

gol.alterarCor("VERDE")
print(gol.cor)

