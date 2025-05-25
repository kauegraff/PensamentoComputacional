from models.ProdutoAlimenticio import ProdutoAlimenticio
from models.ProdutoEletronico import ProdutoEletronico
from models.ConversorMoeda import ConversorMoeda
from utils.Erros import *

nome_produto = input("Digite o nome do produto: ").upper()
preco_produto = float(input("Digite o preço do produto: "))
moeda = input("Qual a moeda do produto [BRL, USD, EUR]?").upper()
tipo_produto = input("Digite o tipo do produto: ").upper()

try: 
    if tipo_produto == "ALIMENTICIO":
        carboidratos = float(input("Digite quantos carboidratos há no produto: "))
        proteinas = float(input("Digite quantas proteínas há no produto: "))
        gorduras_tot = float(input("Digite quantidade de Gorduras que há no produto: "))
        produto_alimenticio = ProdutoAlimenticio(nome_produto, preco_produto, moeda, carboidratos, proteinas, gorduras_tot)
        print("\n****PRODUTO CADASTRADO!****\n")
        print(produto_alimenticio)

    elif tipo_produto == "ELETRONICO":
        volt = float(input("Digite a voltagem do produto: "))
        consumo_energia = float(input("Digite o consumo de energia do produto [W]: "))
        sistema_op = input("Digite o sistema operacional do produto: ").upper()
        produto_eletronico = ProdutoEletronico(nome_produto, preco_produto, moeda, volt, consumo_energia, sistema_op)
        print("\n****PRODUTO CADASTRADO!****\n")
        print(produto_eletronico)
  
    else: 
        raise TipoProdutoInvalidErro("Tipo do Produto digitado inválido!")
    
except TipoProdutoInvalidErro as erro:
    print(f"Ocorreu o erro: {erro}")

print("Novo valor em Dólar")

# Cria uma instância da classe ConversorMoeda
conversor = ConversorMoeda() 
# Converte o produto de rais para dólar
conversor.converte_preco_para_usd(produto_eletronico)

print(produto_eletronico)



