import tkinter as tk
import random

"""def mostrar_texto():
    texto = entrada.get()
    rotulo.config(text=f"Você Digitou: {texto}")

def mostrar_estado():
    if var.get():
        rotulo_check.config(text="Selecionado")
    else:
        rotulo_check.config(text="Não selecionado.")

janela = tk.Tk()
janela.title("Exemplo Entry")
janela.geometry("300x150")

entrada = tk.Entry(janela)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Exibir", command=mostrar_texto)
botao.pack(pady=5)

rotulo = tk.Label(janela, text="")
rotulo.pack(pady=5)

var = tk.BooleanVar()
check = tk.Checkbutton(janela, text="Opção", variable=var, command=mostrar_estado)
check.pack(pady=10)
rotulo_check = tk.Label(janela, text="Não selecionado.")
rotulo_check.pack(pady=5)
janela.mainloop()
"""

def mostrar_opcao(botao):
    rotulo.config(text=f"Escolheu: {botao}")

    if opcao1.get() and opcao2.get() and opcao3.get():
        if botao == "Saúde":
            opcao1.set(False)
            texto = "Dinheiro"
        if botao == "Tempo":
            opcao3.set(False)
            texto = "Saúde"
        if botao == "Dinheiro":
            opcao2.set(False)
            texto = "Tempo"
        rotulo.config(text=f"Você escolheu {botao} e perdeu {texto}")

status = True
janela = tk.Tk()
janela.title("Exemplo Radiobutton")
janela.geometry("250x150")
opcao1 = tk.BooleanVar()
opcao2 = tk.BooleanVar()
opcao3 = tk.BooleanVar()
tk.Radiobutton(janela, text="Tempo", variable=opcao1, value=True, command=lambda: mostrar_opcao("Tempo")).pack()
tk.Radiobutton(janela, text="Dinheiro", variable=opcao2, value=True, command=lambda: mostrar_opcao("Dinheiro")).pack()
tk.Radiobutton(janela, text="Saúde", variable=opcao3, value=True, command=lambda: mostrar_opcao("Saúde")).pack()
rotulo = tk.Label(janela, text="Escolheu: A")
rotulo.pack(pady=10)
janela.mainloop()