class Livro:
    # Classe construtora
    def __init__(self, titulo, autor, ano_publicacao, numero_paginas, pagina_atual):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.pagina_atual = pagina_atual

    # Função para avançar página
    def avancar_pagina(self):
        if self.pagina_atual >= self.numero_paginas:
            print("Você está na última página!")
        else:
            self.pagina_atual += 1
    
    # Função para voltar página
    def voltar_pagina(self):
        if self.pagina_atual > 0:
            self.pagina_atual -= 1
        else:
            print("Você está na primeira página!")
    
    # Função para exibir informações
    def exibir_informacoes(self):
        print(f"\nTítulo: {self.titulo}\n Autor: {self.autor}\n Ano de Publicação: {self.ano_publicacao}\n Número de Páginas: {self.numero_paginas}\n Página Atual: {self.pagina_atual}")