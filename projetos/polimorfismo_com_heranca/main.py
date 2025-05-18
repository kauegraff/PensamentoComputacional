from models.Veiculo import Veiculo
from models.Bicicleta import Bicicleta
from models.Carro import Carro

carro = Veiculo("Chevvete", "Chevrolet", 1990, 0)
bicicleta = Bicicleta("Bicileta Mountain Bike Viking Tuff", "Viking", 2024, 0, 13.5, 26, 21)
monza = Carro("Monza", "Chevrolet", 1986, 0, "Alcool", 95, 4)

lista_veiculos = [carro, bicicleta, monza]
for veiculo in lista_veiculos:
    print(veiculo.mover(3))