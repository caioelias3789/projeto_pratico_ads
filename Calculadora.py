import customtkinter as ctk
from math import sqrt
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.geometry("600x250") # Definindo o tamanho da janela
app.title("Projeto_Calculadora") # Definindo o titulo da janela

# Funções
def inserir_texto(valor):
    entrada.insert("end", valor)

def limpar():
    entrada.delete(0, "end")

def calcular():
    try:
        expressao = entrada.get().replace("x", "*")
        resultado = eval(expressao)
        entrada.delete(0, "end")
        entrada.insert("end", str(resultado))
    except:
        entrada.delete(0, "end")
        entrada.insert("end", "Infinito")

def calcular_raiz():
    try:
        valor = float(entrada.get())
        entrada.delete(0, "end")
        entrada.insert("end", str(sqrt(valor)))
    except:
        entrada.delete(0, "end")
        entrada.insert("end", "Infinito")

def elevar_ao_quadrado():
    try:
        valor = float(entrada.get())
        entrada.delete(0, "end")
        entrada.insert("end", str(valor ** 2))
    except:
        entrada.delete(0, "end")
        entrada.insert("end", "Infinito")

def inverter_numero():
    try:
        valor = float(entrada.get())
        entrada.delete(0, "end")
        entrada.insert("end", str(1 / valor))
    except:
        entrada.delete(0, "end")
        entrada.insert("end", "Infinito")

# Display
entrada = ctk.CTkEntry(app, width=550, height=50, font=("Arial", 20), justify="right")
entrada.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

#botoes dos numeros
botao_usuario0 = ctk.CTkButton(app, text="0", fg_color="#424242", hover_color="#9E9E9E", command=lambda: inserir_texto("0"))
botao_usuario0.grid(row=6, column=2, padx=1, pady=1)

botao_usuario1 = ctk.CTkButton(app, text="1", fg_color="#424242", hover_color="#9E9E9E", command=lambda: inserir_texto("1"))
botao_usuario1.grid(row=5, column=1, padx=1, pady=1)

botao_usuario2 = ctk.CTkButton(app, text="2", fg_color="#424242", hover_color="#9E9E9E", command=lambda: inserir_texto("2"))
botao_usuario2.grid(row=5, column=2, padx=1, pady=1)

botao_usuario3 = ctk.CTkButton(app, text="3", fg_color="#424242", hover_color="#9E9E9E", command=lambda: inserir_texto("3"))
botao_usuario3.grid(row=5, column=3, padx=1, pady=1)

botao_usuario4 = ctk.CTkButton(app, text="4", fg_color="#424242", hover_color="#9E9E9E", command=lambda: inserir_texto("4"))
botao_usuario4.grid(row=4, column=1, padx=1, pady=1)

botao_usuario5 = ctk.CTkButton(app, text="5", fg_color="#424242", hover_color="#9E9E9E", command=lambda: inserir_texto("5"))
botao_usuario5.grid(row=4, column=2, padx=1, pady=1)

botao_usuario6 = ctk.CTkButton(app, text="6", fg_color="#424242", hover_color="#9E9E9E", command=lambda: inserir_texto("6"))
botao_usuario6.grid(row=4, column=3, padx=1, pady=1)

botao_usuario7 = ctk.CTkButton(app, text="7", fg_color="#424242", hover_color="#9E9E9E", command=lambda: inserir_texto("7"))
botao_usuario7.grid(row=3, column=1, padx=1, pady=1)

botao_usuario8 = ctk.CTkButton(app, text="8", fg_color="#424242", hover_color="#9E9E9E", command=lambda: inserir_texto("8"))
botao_usuario8.grid(row=3, column=2, padx=1, pady=1)

botao_usuario9 = ctk.CTkButton(app, text="9", fg_color="#424242", hover_color="#9E9E9E", command=lambda: inserir_texto("9"))
botao_usuario9.grid(row=3, column=3, padx=1, pady=1)

# Botões especiais
botao_usuarioesp0 = ctk.CTkButton(app, text="√", fg_color="#7D8691", hover_color="#606770", command=calcular_raiz)
botao_usuarioesp0.grid(row=2, column=1, padx=1, pady=1)

botao_usuarioesp1 = ctk.CTkButton(app, text=".", fg_color="#424242", hover_color="#9E9E9E", command=lambda: inserir_texto("."))
botao_usuarioesp1.grid(row=6, column=1, padx=1, pady=1)

botao_usuarioesp2 = ctk.CTkButton(app, text="C", fg_color="#b80000", hover_color="#9B0303", command=limpar)
botao_usuarioesp2.grid(row=6, column=3, padx=1, pady=1)

botao_usuarioigual = ctk.CTkButton(app, text="=", fg_color="#005AC7", hover_color="#0263E2", command=calcular)
botao_usuarioigual.grid(row=6, column=4, padx=1, pady=1)

botao_usuarioexpo = ctk.CTkButton(app, text="x²", fg_color="#7D8691", hover_color="#606770", command=elevar_ao_quadrado)
botao_usuarioexpo.grid(row=2, column=3, padx=1, pady=1)

botao_usuarioinverter = ctk.CTkButton(app, text="x/1", fg_color="#7D8691", hover_color="#606770", command=inverter_numero)
botao_usuarioinverter.grid(row=2, column=2, padx=1, pady=1)

# Operadores
botao_usuarioopr1 = ctk.CTkButton(app, text="+", fg_color="#7D8691", hover_color="#606770", command=lambda: inserir_texto("+"))
botao_usuarioopr1.grid(row=5, column=4, padx=1, pady=1)

botao_usuarioopr2 = ctk.CTkButton(app, text="-", fg_color="#7D8691", hover_color="#606770", command=lambda: inserir_texto("-"))
botao_usuarioopr2.grid(row=4, column=4, padx=1, pady=1)

botao_usuarioopr3 = ctk.CTkButton(app, text="x", fg_color="#7D8691", hover_color="#606770", command=lambda: inserir_texto("x"))
botao_usuarioopr3.grid(row=3, column=4, padx=1, pady=1)

botao_usuarioopr4 = ctk.CTkButton(app, text="/", fg_color="#7D8691", hover_color="#606770", command=lambda: inserir_texto("/"))
botao_usuarioopr4.grid(row=2, column=4, padx=1, pady=1)

app.mainloop()