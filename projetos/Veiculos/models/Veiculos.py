class Veiculos:
    def __init__(self, modelo, marca, ano, cor, velocidade, placa, latitude, longitude):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
        self.placa = placa
        self.latitude = latitude
        self.longitude = longitude

    def acelerar(self):
        self.velocidade += 10
        nova_latidude = self.latitude + 1
        self.alterarLatitude(nova_latidude)
        print(f"O carro de placa {self.placa} foi acelerado até {self.velocidade} Km/h") 
        
    def desacelerar(self):
        if self.velocidade > 0:
            self.velocidade -= 10
    
    def exibirInfos(self):
        print(f"O Véiculo {self.modelo} de placa {self.placa} está a {self.velocidade} km/h")
        print(f"Latitude: {self.latitude}, Longitude: {self.longitude}")

    def alterarModelo(self, modelo):
        self.modelo = modelo
    
    def alterarMarca(self, marca):
        self.marca = marca
    
    def alterarAno(self, ano):
        self.ano = ano
    
    def alterarCor(self, cor):
        self.cor = cor
    
    def alterarLatitude(self, latitude):
        self.latitude = latitude
    
    def alterarLongitude(self, longitude):
        self.longitude = longitude

    def alterarPlaca(self, placa):
        self.placa = placa

    def obterPlaca(self):
        return self.placa
    
