# Algoritmo de catalogo de filmes

def titulo_principal():
   return print("""
  ____      _        _
 / ___|__ _| |_ __ _| | ___   __ _  ___
| |   / _` | __/ _` | |/ _ \ / _` |/ _ \
| |__| (_| | || (_| | | (_) | (_| | (_) |
 \____\__,_|\__\__,_|_|\___/ \__, |\___/
                             |___/

 ____  _____
|  _ \| ____|
| | | |  _|
| |_| | |___
|____/|_____|


 _____ _ _
|  ___(_) |_ __ ___   ___  ___
| |_  | | | '_ ` _ \ / _ \/ __|
|  _| | | | | | | | |  __/\__ \
|_|   |_|_|_| |_| |_|\___||___/


""")

def titulo_top_tres():

  return print("""

 _____ ___  ____    _____
|_   _/ _ \|  _ \  |___ /
  | || | | | |_) |   |_ \
  | || |_| |  __/   ___) |
  |_| \___/|_|     |____/

""")

def imagem_final_walace():
  return print("""

    ."'=-,     ,.,.,_
   (_____ )."=`      `"=,
  ./_ _  \`\             `;..
 / (o(o) |\=\              ; `;
(_/|     | \ |             ;`"`
   |     |  `             ;
   \ ..  /`,_          _.'
    `---'   `#"#""'"#'#^
             # #    # #
             # #    # #
             # #    # #
             # #    # #
             # #    # #
       jgs  /#|#\  /#|#\
            `"`"`  `"`"`

""")

titulo_principal()

def remove_filme(filmes):
  # Seleciona o filme que deseja remover
  filme_del = input("Digite o filme que deseja remover: ").title()
  for filme in filmes:
    if filme["nome"] == filme_del:
      # Pega o indice em que está o dicionario do filme
      index_remove = filmes.index(filme)
      # Remove o dicionario em que está o filme
      del filmes[index_remove]
      print("Filme Removido da Lista")
      break
  else:
    print("Filme digitado não foi cadastrado ainda!")

def duplicidade(novo, filmes):
  for filme in filmes:
    # Verifica se o filme digitado já existe na lista
    if novo == filme["nome"]:
      return True
  return False

def media(filmes):
  # Conta o tamanho da lista
  cnt = len(filmes)
  # Se a contagem for igual a zero retorna zero
  if cnt == 0:
    return 0
  soma = 0
  for filme in filmes:
    # soma as notas dos filmes
    soma += filme["nota"]
    # Retorna o cálculo da média
  return round(soma/cnt, 1)

# Imprime a lista de filmes
def imprime_filmes(filmes):
  for filme in filmes:
    print(f"O filme {filme['nome']} teve nota {filme['nota']}")

def edita_filme(filmes):
  # Entrada do filme que será alterado
  filme_edit = input("Digite o filme que você deseja alterar:").title()
  for filme in filmes:
    # Verifica se o filme digitado existe na lista
    if filme['nome'] == filme_edit:
      # Seleciona o novo nome
      novo_nome = input("Digite o novo nome do filme: ")
      # Seleciona a nova nota
      nova_nota = float(input("Digite a nova nota do filme: "))
      # Solicita a entrada de uma nova nota até que o usuário digite um número
      while not isinstance(nova_nota, float):
        nova_nota = input("A nota precisa ser um número! Tente novamente: ")
      # Subsitui a nota e o nome
      filme['nota'] = nova_nota
      filme['nome'] = novo_nome.title()
      print("Filme alterado com sucesso")
  else:
    print("Filme não existe na lista!")

def cadastro(filmes):
  # Entrada do nome e da nota
  filme = input("Digite o nome do filme: ").title()
  nota = float(input("Digite a nota do filme: "))
  while not isinstance(nota, float):
    nota = input("A nota precisa ser um número! Tente novamente: ")
  # Verifica se o filme digitado existe na lista
  if duplicidade(filme, filmes):
      print(f"\nO filme {filme}, já foi cadastrado")
  else:
    # Adiciona o filme e a nota na lista
    print("Filme Cadastrado Com Sucesso!")
    return filmes.append({"nome": filme, "nota": nota})

# Função que pega os três melhores filmes
def exibe_top3(filmes):
  lista_ordenada = sorted(filmes, key=lambda filme: filme['nota'], reverse=True)
  return lista_ordenada[:3]


# Lista de Filmes
lista_filmes = []

string = "\n "
string += "-"*20
string += "\nDigite: add para cadastrar um filme"
string += "\n      rm para remover um filme"
string += "\n      ed para editar um filme"
string += "\n      sa para sair"
string += "\n "
string += "-"*20

while True:
  # Verifica o tamanho da lista de filmes
    if len(lista_filmes) > 1000:
      break
    else:
      print(string)
      # Entrada da operação que o usuário deseja
      operacao = input(" ").lower()
      # Verifica a operação do usuário
      if operacao == "add":
        cadastro(lista_filmes)
      # Remove um filme da lista
      elif operacao == "rm":
        remove_filme(lista_filmes)
      # Edita um filme
      elif operacao == "ed":
        edita_filme(lista_filmes)
      # Saí do sistema
      elif operacao == "sa":
        print("\nSistema finalizado pelo usuário!")
        break

# Imprime a lista de filmes com as notas
print("\n")

# Imprime as listas de filme
imprime_filmes(lista_filmes)
print(f"\nA nota média dos filmes é: {media(lista_filmes)}")

# Imprime o título TOP 3
titulo_top_tres()

for filme in exibe_top3(lista_filmes):
  print(f"Filme: {filme['nome']}, Nota: {filme['nota']}")

# Imprime o Walace como mensagem final
imagem_final_walace()

