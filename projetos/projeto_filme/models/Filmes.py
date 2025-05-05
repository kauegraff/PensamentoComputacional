class Filme:
    def __init__(self, titulo, genero, duracao, avaliacao):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.avaliacao = avaliacao
    
    def avaliar(self, nota):
        if nota > 10 or nota < 0:
            print("Nota Inválida! A nota deve ser entre 0 e 10")
        else:
            self.avaliacao = nota
    
    def exibir_informacoes(self):
        print(f"Titulo: {self.titulo}, Gênero: {self.genero}, Duração: {self.duracao}, Avaliação: {self.avaliacao}")
          