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
app.mainloop()