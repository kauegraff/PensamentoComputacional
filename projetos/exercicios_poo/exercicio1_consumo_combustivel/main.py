from models.Veiculo import Veiculo
from models.Caminhao import Caminhao
from models.Moto import Moto
from models.Carro import Carro

moto = Moto("INS7108", "CG 150", "Vermelha", "Honda", 2009, 13000)
caminhao = Caminhao("INS7108", "1113", "Amarelo", "Mercedes", 1981, 38755)
carro = Carro("INS7108", "CIVIC", "PRATA", "HONDA", 2007, 38280)

lista_veiculos = [moto, caminhao, carro]

distancia = float(input("Digite a distância percorrida pelo veículo: "))

for veiculo in lista_veiculos:
    print(veiculo.calcular_consumo(distancia))
