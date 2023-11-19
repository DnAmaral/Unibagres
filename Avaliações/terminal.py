import tkinter as tk
from tkinter import messagebox

# Função para exibir a mensagem em uma nova janela;
def enviar_mensagem():
    nome = nome_entry.get()
    mensagem = mensagem_entry.get()

    if nome and mensagem:
        mensagem_completa = f"Nome: {nome}\nMensagem: {mensagem}"
        messagebox.showinfo("Resultado", mensagem_completa)
    else:
        messagebox.showerror("Erro", "Por favor, preencha ambos os campos.")

# Criar a janela principal;
root = tk.Tk()
root.title("Envio de Mensagem")

# Label e campo de entrada para o nome
nome_label = tk.Label(root, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

# Label e campo de entrada para a mensagem
mensagem_label = tk.Label(root, text="Mensagem:")
mensagem_label.pack()
mensagem_entry = tk.Entry(root)
mensagem_entry.pack()

# Botão "Enviar" para exibir a mensagem
enviar_button = tk.Button(root, text="Enviar", command=enviar_mensagem)
enviar_button.pack()

# Loop para interface gráfica!
root.mainloop()