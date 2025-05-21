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
tesla_model = VeiculoEletrico("LKS2345", "TESLA MODEL S", "PRATA", "TESLA", 2024, 414000)

lista_veiculos = [moto, caminhao, carro, chevette, tesla_model]

# Entrada da distância
distancia = float(input("Digite a distância percorrida pelo veículo: "))

# Criando o objeto frota
frota = Frota(moto)

# Adicionando um veículo na frota
frota.adicionar_veiculo(chevette)
frota.adicionar_veiculo(caminhao)
frota.adicionar_veiculo(carro)

# Percorre a lista de veículos e calcula o consumo de cada um
for veiculo in lista_veiculos:
    print(veiculo.calcular_consumo(distancia))

# Exibe a lista de veículos da frota
print(frota.exibir_frota())

# Mostra o total de combustível da frota
print(f"O consumo total da frota foi de {round(frota.calcular_consumo(distancia), 2)} litros")

# Altera a placa do carro
chevette.setPlaca("CBA")

# Mostra a placa do carro
print(chevette.getPlaca())

# Verifica se a placa já exista, retorna true se a placa já existe
print(moto == caminhao)





