import tkinter  # En esta parte se importo lo necesario
import customtkinter
from usuarios_p.registro_usuario import registrar
from usuarios_p.visualizar_usuarios import visualizar
from usuarios_p.deshabilitar_usuario import desabilitar
from usuarios_p.login_cambios_usuarios import login_cambios
from usuarios_p.double_list import DoubleList

lista_usuarios = None  # Se llamo a la lista


def main_user(lista_users: DoubleList):
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Usuario")
    app.geometry("800x400")

    global lista_usuarios
    lista_usuarios = lista_users

    button2 = customtkinter.CTkButton(master=app, text="Visualizar usuarios",
                                      command=mostrar)  # Se crean los botones con
    # sus funciones respectivas
    button2.place(relx=0.25, rely=0.25, anchor=tkinter.CENTER)
    button3 = customtkinter.CTkButton(master=app, text="Registrar usuario", command=registro)
    button3.place(relx=0.65, rely=0.25, anchor=tkinter.CENTER)
    button4 = customtkinter.CTkButton(master=app, text="Cambios", command=datos_cambio)
    button4.place(relx=0.25, rely=0.45, anchor=tkinter.CENTER)
    button6 = customtkinter.CTkButton(master=app, text="Desabilitar usuarios", command=deshavili)
    button6.place(relx=0.65, rely=0.45, anchor=tkinter.CENTER)

    app.mainloop()  # Para iniciar la ventana


def registro(): # Funció para ir a la ventana de registro
    global lista_usuarios
    registrar(lista_usuarios)


def mostrar():  # Función para ir a la ventana de visualizar
    global lista_usuarios

    visualizar(lista_usuarios)


def deshavili():  # Función para ir a la ventana de desabilitar
    global lista_usuarios

    desabilitar(lista_usuarios)


def datos_cambio():  # Función para ir a la ventana de login
    global lista_usuarios

    login_cambios(lista_usuarios)
