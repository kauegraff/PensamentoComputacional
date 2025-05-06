class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade 
        self.altura = altura
    
    def aniversario(self):
        self.idade += 1

    def crescer(self, valor):
        self.altura += valor
    
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}")