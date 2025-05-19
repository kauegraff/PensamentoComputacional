from models.Frota import Frota
from models.Veiculo import Veiculo

moto = Veiculo("INS7108", "CG 150", "Vermelha", "Honda", 2009, 13000)
caminhao = Veiculo("INS7108", "1113", "Amarelo", "Mercedes", 1981, 38755)
carro = Veiculo("INS7108", "CIVIC", "PRATA", "HONDA", 2007, 38280)
chevette = Veiculo("ABC1234", "Chevette", "Preto", "Chevrolet", 1990, 15000)

lista_veiculos = [moto, caminhao, carro]

frota = Frota(lista_veiculos)

print(frota.exibir_frota())

frota.adicionar_veiculo(chevette)

print(frota.exibir_frota())