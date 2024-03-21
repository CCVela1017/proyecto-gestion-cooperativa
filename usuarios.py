import tkinter  # En esta parte se importo lo necesario
import customtkinter
from registro_usuario import registrar
from visualizar_usuarios import visualizar
from listadobleenlace import List
from class_usuario import Usuarios
from deshabilitar_usuario import desabilitar
from login_cambios_usuarios import login_cambios

lista_usuarios = List[Usuarios]()  # Se llamo a la lista

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Usuario")
app.geometry("800x400")


def registro():  # Funció para ir a la ventana de registro
    registrar(lista_usuarios)


def mostrar():  # Función para ir a la ventana de visualizar
    visualizar(lista_usuarios)


def deshavili():  # Función para ir a la ventana de desabilitar
    desabilitar(lista_usuarios)


def datos_cambio():  # Función para ir a la ventana de login
    login_cambios(lista_usuarios)


button2 = customtkinter.CTkButton(master=app, text="Visualizar usuarios", command=mostrar)  # Se crean los botones con
# sus funciones respectivas
button2.place(relx=0.25, rely=0.25, anchor=tkinter.CENTER)
button3 = customtkinter.CTkButton(master=app, text="Registrar usuario", command=registro)
button3.place(relx=0.65, rely=0.25, anchor=tkinter.CENTER)
button4 = customtkinter.CTkButton(master=app, text="Cambios", command=datos_cambio)
button4.place(relx=0.25, rely=0.45, anchor=tkinter.CENTER)
button6 = customtkinter.CTkButton(master=app, text="Desabilitar usuarios", command=deshavili)
button6.place(relx=0.65, rely=0.45, anchor=tkinter.CENTER)


app.mainloop()  # Para iniciar la ventana
