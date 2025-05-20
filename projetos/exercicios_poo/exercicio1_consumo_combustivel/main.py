from models.Veiculo import Veiculo
from models.Caminhao import Caminhao
from models.Moto import Moto
from models.Carro import Carro
from models.Frota import Frota
from models.VeiculoEletrico import VeiculoEletrico

# Criando os objetos com as classes que herdas de veículo
moto = Moto("INS7108", "CG 150", "Vermelha", "Honda", 2009, 13000)
caminhao = Caminhao("INS7108", "1113", "Amarelo", "Mercedes", 1981, 38755)
carro = Carro("INS7108", "CIVIC", "PRATA", "HONDA", 2007, 38280)
chevette = Carro("ABC1234", "Chevette", "Preto", "Chevrolet", 1990, 15000)
tesla = VeiculoEletrico()
# Adicionando os veículos na lista
lista_veiculos = [moto, caminhao, carro]

# Entrada da distância
distancia = float(input("Digite a distância percorrida pelo veículo: "))

# Percorre a lista de veículos e calcula o consumo de cada um
for veiculo in lista_veiculos:
    print(veiculo.calcular_consumo(distancia))

lista_veiculos = [moto, caminhao, carro]

# Criando o objeto frota
frota = Frota(lista_veiculos)

# Adicionando um veículo na frota
frota.adicionar_veiculo(chevette)

# Exibe a lista de veículos da frota
print(frota.exibir_frota())

# Mostra o total de combustível da frota
print(f"O consumo total da frota foi de {round(frota.calcular_consumo(distancia), 2)} litros")
