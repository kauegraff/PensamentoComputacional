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
janela.mainloop()"""

def mostrar_opcao():
    global status
    texto = f"{opcao1.get()}"
    texto += f"{opcao2.get()}"
    texto += f"{opcao3.get()}"
    rotulo.config(text=texto)

    op = [opcao1.get(), opcao2.get(), opcao3.get()]
    if op.count(True) == 3:
        rand = random.randint(0, 2)
        if rand == 0:
            opcao1.set(False)
        if rand == 1:
            opcao2.set(False)
        if rand == 2:
            opcao3.set(False)


status = True
janela = tk.Tk()
janela.title("Exemplo Radiobutton")
janela.geometry("250x150")
opcao1 = tk.BooleanVar()
opcao2 = tk.BooleanVar()
opcao3 = tk.BooleanVar()
tk.Radiobutton(janela, text="Tempo", variable=opcao1, value=True, command=mostrar_opcao).pack()
tk.Radiobutton(janela, text="Dinheiro", variable=opcao2, value=True, command=mostrar_opcao).pack()
tk.Radiobutton(janela, text="Saúde", variable=opcao3, value=True, command=mostrar_opcao).pack()
rotulo = tk.Label(janela, text="Escolheu: A")
rotulo.pack(pady=10)
janela.mainloop()