import customtkinter as ctk
from math import sqrt
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.geometry("600x250") # Definindo o tamanho da janela
app.title("Projeto_Calculadora") # Definindo o titulo da janela

#botoes dos numeros
botao_usuario0 = ctk.CTkButton(app, text="0",fg_color="#424242",hover_color="#9E9E9E", command="") 
botao_usuario0.grid(row=6, column=2, padx=1, pady=1) 

botao_usuario1 = ctk.CTkButton(app, text="1",fg_color="#424242",hover_color="#9E9E9E", command="") 
botao_usuario1.grid(row=5, column=1, padx=1, pady=1) 

botao_usuario2 = ctk.CTkButton(app, text="2",fg_color="#424242",hover_color="#9E9E9E", command="") 
botao_usuario2.grid(row=5, column=2, padx=1, pady=1) 

botao_usuario3 = ctk.CTkButton(app, text="3",fg_color="#424242",hover_color="#9E9E9E", command="") 
botao_usuario3.grid(row=5, column=3, padx=1, pady=1) 

botao_usuario4 = ctk.CTkButton(app, text="4",fg_color="#424242",hover_color="#9E9E9E", command="") 
botao_usuario4.grid(row=4, column=1, padx=1, pady=1) 

botao_usuario5 = ctk.CTkButton(app, text="5",fg_color="#424242",hover_color="#9E9E9E", command="") 
botao_usuario5.grid(row=4, column=2, padx=1, pady=1) 

botao_usuario6 = ctk.CTkButton(app, text="6",fg_color="#424242",hover_color="#9E9E9E", command="") 
botao_usuario6.grid(row=4, column=3, padx=1, pady=1) 

botao_usuario7 = ctk.CTkButton(app, text="7",fg_color="#424242",hover_color="#9E9E9E", command="") 
botao_usuario7.grid(row=3, column=1, padx=1, pady=1) 

botao_usuario8 = ctk.CTkButton(app, text="8",fg_color="#424242",hover_color="#9E9E9E", command="") 
botao_usuario8.grid(row=3, column=2, padx=1, pady=1) 

botao_usuario9 = ctk.CTkButton(app, text="9",fg_color="#424242",hover_color="#9E9E9E", command="") 
botao_usuario9.grid(row=3, column=3, padx=1, pady=1) 

#botoes especiais
botao_usuarioesp0 = ctk.CTkButton(app, text="√",fg_color="#7D8691",hover_color="#606770", command=lambda: print(sqrt()))
botao_usuarioesp0.grid(row=2, column=1, padx=1, pady=1)

botao_usuarioesp1 = ctk.CTkButton(app, text=".",fg_color="#424242",hover_color="#9E9E9E", command="") 
botao_usuarioesp1.grid(row=6, column=1, padx=1, pady=1) 

botao_usuarioesp2 = ctk.CTkButton(app, text="C",fg_color="#b80000",hover_color="#9B0303", command="")
botao_usuarioesp2.grid(row=6, column=3, padx=1, pady=1)

botao_usuarioigual = ctk.CTkButton(app, text="=",fg_color="#005AC7",hover_color="#0263E2", command="") 
botao_usuarioigual.grid(row=6, column=4, padx=1, pady=1) 

botao_usuarioexpo = ctk.CTkButton(app, text="x²",fg_color="#7D8691",hover_color="#606770", command="")
botao_usuarioexpo.grid(row=2, column=3, padx=1, pady=1)

botao_usuarioinverter = ctk.CTkButton(app, text="x/1",fg_color="#7D8691",hover_color="#606770", command="")
botao_usuarioinverter.grid(row=2, column=2, padx=1, pady=1)
#botoes de operacoes
botao_usuarioopr1 = ctk.CTkButton(app, text="+",fg_color="#7D8691",hover_color="#606770", command="") 
botao_usuarioopr1.grid(row=5, column=4, padx=1, pady=1) 

botao_usuarioopr2 = ctk.CTkButton(app, text="-",fg_color="#7D8691",hover_color="#606770", command="") 
botao_usuarioopr2.grid(row=4, column=4, padx=1, pady=1) 

botao_usuarioopr3 = ctk.CTkButton(app, text="x",fg_color="#7D8691",hover_color="#606770", command="") 
botao_usuarioopr3.grid(row=3, column=4, padx=1, pady=1) 

botao_usuarioopr4 = ctk.CTkButton(app, text="/",fg_color="#7D8691",hover_color="#606770", command="")
botao_usuarioopr4.grid(row=2, column=4, padx=1, pady=1)
app.mainloop()