from models.Veiculos import Veiculos
from models.CarrosCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletrico import CarroConvEletrico

voyage = Veiculos("BCE9D36", "Voyage", "Vermelho", 
                  "Volkswagen", 2018, 47793)

jetta_gli = CarroCombustao("JDM9D36", "Jetta GLI", "Vermelho", 
                           "Volkswagen", 2025, 250000, "Gasolina", 4, 5, 2000, "AT 7", 24)

tesla_model_s = CarroEletrico("JDN0A00", "Tesla Model S", "Branco", 
                              "Tesla", 2021, 950000, 5, 4, 
                               65, "Lítio", 491)

fusca_eletrico = CarroConvEletrico(placa="IAA0D36", modelo="Fusca 1600 Elétrico", cor="Azul", 
                                    marca="Volkswagen", ano=1975, valor_fipe=70000, 
                                    combustivel="Gasolina", nPortas=4, nAssentos=5, 
                                    nCilindradas=1600, nCambio="MT 4", nivel_combustivel=24, 
                                    nivel_bateria=65, tipo_bateria="Lítio", autonomia=150)

print(jetta_gli)

if jetta_gli.abastecer(100):
    print("Abastecido com sucesso!")
else:
    print("Erro ao abastecer")

print(fusca_eletrico)

fusca_eletrico.abastecer(10)

print(fusca_eletrico)




