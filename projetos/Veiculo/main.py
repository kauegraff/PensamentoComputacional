from models.Veiculos import Veiculos
from models.CarrosCombustao import CarroCombustao

voyage = Veiculos("BCE9D36", "Voyage", "Vermelho", 
                  "Volkswagen", 2018, 47793)

print(voyage)

jetta_gli = CarroCombustao("JDM9D36", "Jetta GLI", "Vermelho", "Volkswagen", 2025, 250000, "Gasolina", 4, 5, 2000, "AT 7")
print(jetta_gli)