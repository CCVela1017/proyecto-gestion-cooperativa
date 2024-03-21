import tkinter  # En esta parte se importo lo necesario
import customtkinter
from data_structures.double_list import DoubleList
from class_usuario import Usuarios
import random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def registrar(listausuario: List):  # En esta parte se creo la funcion para mostrar la ventana de registro
    regis = customtkinter.CTk()
    regis.title("Regristro de usuarios")
    regis.geometry("800x400")
    lista_usuarios = listausuario

    def ingresar():  # Función para poder agregar un numero unico y guardar datos
        comprovar = True
        while comprovar:
            codigo_completo1 = random.randrange(1, 100)
            if len(lista_usuarios) >= 1:
                data = []
                for n in lista_usuarios:
                    data.append([n.codigo, n.nombre, n.correo, n.contrasena, n.puesto, n.estado])
                z = 0
                for ver in data:
                    if int(ver[0]) == int(codigo_completo1):
                        z += 1

                if z == 0:
                    usuarios = Usuarios(codigo_completo1, nombre_completo1.get(), correoelectronico1.get(),
                                        contrasenas1.get(), puesto2.get(), estado2.get())
                    lista_usuarios.append(usuarios)
                    comprovar = False
            else:
                usuarios = Usuarios(codigo_completo1, nombre_completo1.get(), correoelectronico1.get(),
                                    contrasenas1.get(), puesto2.get(), estado2.get())
                lista_usuarios.append(usuarios)
                comprovar = False

    nombre_completo = customtkinter.CTkLabel(master=regis, text="Nombre completo")  # En esta parte se crean los Label y
    # Entry para colocar el correo nombre y contraseña en su sitio
    nombre_completo.place(relx=0.25, rely=0.25, anchor=tkinter.CENTER)

    correoelectronico = customtkinter.CTkLabel(master=regis, text="Correo electronica")
    correoelectronico.place(relx=0.25, rely=0.35, anchor=tkinter.CENTER)

    contrasenas = customtkinter.CTkLabel(master=regis, text="Contraseña")
    contrasenas.place(relx=0.25, rely=0.45, anchor=tkinter.CENTER)

    puesto1 = customtkinter.CTkLabel(master=regis, text="Puesto")
    puesto1.place(relx=0.25, rely=0.55, anchor=tkinter.CENTER)

    estado1 = customtkinter.CTkLabel(master=regis, text="Estado")
    estado1.place(relx=0.25, rely=0.65, anchor=tkinter.CENTER)

    nombre_completo1 = customtkinter.CTkEntry(master=regis)
    nombre_completo1.place(relx=0.45, rely=0.25, anchor=tkinter.CENTER)

    correoelectronico1 = customtkinter.CTkEntry(master=regis)
    correoelectronico1.place(relx=0.45, rely=0.35, anchor=tkinter.CENTER)

    contrasenas1 = customtkinter.CTkEntry(master=regis)
    contrasenas1.place(relx=0.45, rely=0.45, anchor=tkinter.CENTER)

    puesto2 = customtkinter.CTkEntry(master=regis)
    puesto2.place(relx=0.45, rely=0.55, anchor=tkinter.CENTER)

    estado2 = customtkinter.CTkEntry(master=regis)
    estado2.place(relx=0.45, rely=0.65, anchor=tkinter.CENTER)

    boton1 = customtkinter.CTkButton(master=regis, text="Ingresar", command=ingresar)  # Boton para llamar la acción
    boton1.place(relx=0.7, rely=0.25, anchor=tkinter.CENTER)

    regis.mainloop()  # Para iniciar la ventana
