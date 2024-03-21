import tkinter   # En esta parte se importo lo necesario
import customtkinter
from data_structures.double_list import DoubleList
from usuarios_p.datos_usuario import cambio_datos
from usuarios_p.cambio_contraseñas_usuarios import cambio_contrasena

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def login_cambios(listausuario: DoubleList):  # En esta parte se creo la funcion para mostrar la ventana de cambios
    login = customtkinter.CTk()
    login.title("Login")
    login.geometry("800x400")
    lista_usuarios = listausuario

    def datos_cambiar():  # En esta funcion se hace la verificación del correo y contraseña para poder ingresar al
        # apartado de cambios
        data = []
        for n in lista_usuarios:
            data.append([n.codigo, n.nombre, n.correo, n.contrasena, n.puesto, n.estado])

        for datos in data:
            if (str(datos[2]) == (nombre_completo1.get())) and (str(datos[3]) == str(correoelectronico1.get())):
                cambio_datos(listausuario)

    def cambio_contrasenas():  # En esta función se hace la verificación del correo y contraseña par pode ingresar al
        # apartado de contraseñas
        data = []
        for n in lista_usuarios:
            data.append([n.codigo, n.nombre, n.correo, n.contrasena, n.puesto, n.estado])

        for datos in data:
            if (str(datos[2]) == (nombre_completo1.get())) and (str(datos[3]) == str(correoelectronico1.get())):
                cambio_contrasena(listausuario)

    nombre_completo = customtkinter.CTkLabel(master=login, text="Correo")  # En esta parte se crean los Label y Entry
    # para colocar el correo nombre y contraseña en su sitio
    nombre_completo.place(relx=0.25, rely=0.25, anchor=tkinter.CENTER)

    correoelectronico = customtkinter.CTkLabel(master=login, text="Contraseña")
    correoelectronico.place(relx=0.25, rely=0.35, anchor=tkinter.CENTER)

    nombre_completo1 = customtkinter.CTkEntry(master=login)
    nombre_completo1.place(relx=0.45, rely=0.25, anchor=tkinter.CENTER)

    correoelectronico1 = customtkinter.CTkEntry(master=login)
    correoelectronico1.place(relx=0.45, rely=0.35, anchor=tkinter.CENTER)

    boton1 = customtkinter.CTkButton(master=login, text="Actualizar datos", command=datos_cambiar)
    boton1.place(relx=0.7, rely=0.25, anchor=tkinter.CENTER)

    boton1 = customtkinter.CTkButton(master=login, text="Actualizar contraseñas", command=cambio_contrasenas)
    boton1.place(relx=0.7, rely=0.35, anchor=tkinter.CENTER)

    login.mainloop()  # Para iniciar la ventana
