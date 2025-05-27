import tkinter as tk
from tkinter import ttk

def mensagem():
    if rotulo["text"] == "Olá, Mundo!":
        rotulo.config(text="Olá, Turma!")
    else:
        rotulo.config(text="Olá, Mundo!")

janela = tk.Tk()
janela.title("Minha Primeira Janela")
rotulo = tk.Label(janela, text="Bem-vindo ao Tkinter", font=("Arial", 26))
rotulo.pack(padx=20, pady=20)
botao = tk.Button(janela, text="Clique no botão abaixo", font=("Arial", 26), command=mensagem)
botao.pack(pady=10)
janela.geometry("300x200") 
janela.mainloop()




