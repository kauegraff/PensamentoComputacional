from models.Veiculo import Veiculo
from models.Caminhao import Caminhao
from models.Moto import Moto
from models.Carro import Carro
from models.Frota import Frota
from models.VeiculoEletrico import VeiculoEletrico
from utils.Erros import *

def validar_placa(placa):
    try:
        if placa[:3].isalpha() and placa[3:4].isnumeric() and placa[4:5].isalpha() and placa[5:].isnumeric():
            return True
        else:
            raise PlacaInvalida("Placa inválida!")
        
    except PlacaInvalida as erro:
        print(f"Ocorreu o Erro: {erro}")     
        return False  

def cadastrar_veiculo():
    placa = input("Digite a placa do veículo: ")
    while validar_placa(placa) == False:
        placa = input("Digite a placa do veículo: ")

# Criando os objetos com as classes que herdas de veículo
moto = Moto("INS7108", "CG 150", "Vermelha", "Honda", 2009, 13000)
caminhao = Caminhao("INS7108", "1113", "Amarelo", "Mercedes", 1981, 38755)
carro = Carro("INS7108", "CIVIC", "PRATA", "HONDA", 2007, 38280)
chevette = Carro("ABC1234", "Chevette", "Preto", "Chevrolet", 1990, 15000)
tesla_model = VeiculoEletrico("LKS2345", "TESLA MODEL S", "PRATA", "TESLA", 2024, 414000)

lista_veiculos = [moto, caminhao, carro, chevette, tesla_model]

cadastrar_veiculo()

# Trata os erros de tipo de veículo e distância negativa ou inválida
try:
    # Entrada da distância
    distancia = float(input("Digite a distância percorrida pelo veículo: "))
    tipo_veiculo = input("Digite o tipo de veículo (Carro, Moto, Caminhão): ")

    if distancia < 0:
        raise DistanciaNegativa("A distância não pode ser negaiva.")
    
    for objeto in lista_veiculos:
        if objeto.__class__.__name__ == tipo_veiculo:
            print("Tipo de veículo existente")
            print(f"Veículo {objeto.getModelo()} é do tipo {tipo_veiculo}\n")
    else:
        raise VeiculoInexistente("O tipo de veículo digitado não existe.")
except ValueError as erro:
    print(f"Erro: {erro}")
except DistanciaNegativa as erro:
    print(f"Erro: {erro}")
except VeiculoInexistente as erro:
    print(f"Erro: {erro}")

# Criando o objeto frota
frota = Frota(moto)

# Adicionando um veículo na frota
frota.adicionar_veiculo(chevette)
frota.adicionar_veiculo(caminhao)
frota.adicionar_veiculo(carro)

# Percorre a lista de veículos e calcula o consumo de cada um e trata uma possível lista vazia
try:
    if len(lista_veiculos) > 0:
        for veiculo in lista_veiculos:
            if isinstance(veiculo, (Carro, Moto, Caminhao)):
                print(f"\nO veículo {veiculo.getModelo()} Teve consumo de {veiculo.calcular_consumo(distancia)} Litros")
            else: 
                print(f"\nO veículo {veiculo.getModelo()} Teve consumo de {veiculo.calcular_consumo(distancia)} kWh")
    else:
        raise ListaVazia("A lista de veiculos está vazia")
except ListaVazia as erro:
    print(f"Ocorreu o Erro: {erro}")

# Exibe a lista de veículos da frota
frota.exibir_frota()

# Mostra o total de combustível da frota
print(f"O consumo total da frota foi de {round(frota.calcular_consumo(distancia), 2)} litros\n")

# Altera a placa do carro
chevette.setPlaca("INS7A08")

# Mostra a placa do carro
print("\nMOSTRA A NOVA PLACA DO VEÍCULO")
print(chevette.getPlaca())

# Verifica se a placa já exista, retorna true se a placa já existe
print("\nVERIFICA SE A PLACA DE UM OBJETO JÁ EXISTE")
print(moto == caminhao)





