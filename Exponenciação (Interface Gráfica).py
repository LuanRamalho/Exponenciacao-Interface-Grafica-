import tkinter as tk
from tkinter import messagebox

# Função para calcular as exponenciações
def calcular_exponenciacoes():
    try:
        num = int(entry_num.get())  # Obtém o número inserido no campo de texto
        
        # Exponenciações de 1 até 10
        resultados = [num**i for i in range(1, 11)]
        
        # Exibir resultados
        result_text.set("\n".join([f"{num} elevado à {i}: {resultados[i-1]}" for i in range(1, 11)]))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número inteiro válido.")

# Função para alterar a cor do botão ao passar o mouse (efeito hover)
def on_enter(e):
    btn_calcular.config(bg="#45a049")

def on_leave(e):
    btn_calcular.config(bg="#4CAF50")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de Exponenciações")

# Configurando a aparência da janela
root.geometry("500x500")
root.configure(bg="greenyellow")

# Título
titulo = tk.Label(root, text="Calculadora de Exponenciações", font=("Arial", 18, "bold"), bg="teal", fg="white", pady=10)
titulo.pack(fill=tk.X, padx=20, pady=10)

# Campo de entrada para o número
entrada_label = tk.Label(root, text="Digite um número inteiro:", font=("Arial", 12), bg="greenyellow", fg="#333333")
entrada_label.pack(pady=10)

entry_num = tk.Entry(root, font=("Arial", 14), width=25, bd=2, relief="solid", justify="center", fg="#333333")
entry_num.pack(pady=10)

# Botão para calcular
btn_calcular = tk.Button(root, text="Calcular", font=("Arial", 14, "bold"), bg="purple", fg="white", width=20, height=2, relief="raised", command=calcular_exponenciacoes)
btn_calcular.pack(pady=15)

# Efeitos hover no botão
btn_calcular.bind("<Enter>", on_enter)
btn_calcular.bind("<Leave>", on_leave)

# Label para exibir os resultados
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), bg="maroon", fg="honeydew", justify="center", width=30)
result_label.pack(pady=10)

# Iniciar a interface gráfica
root.mainloop()
