import customtkinter
from tkinter import filedialog
from data_structures.list import List
import random
from asociados.asociado import Asociado

gestion: List[Asociado]
ref = List[str]()

ventana = customtkinter.CTk()  # Crea ventana principal
ventana2 = customtkinter.CTk()


def cerrar_ventana1():
    ventana.withdraw()  # ocultar ventana 1
    ventana2.deiconify()


def agregar_referencia():
    w3 = customtkinter.CTkToplevel()
    w3.configure(background="white")
    w3.title("Agregar Referencia")
    w3.geometry("400x300")

    mensaje = customtkinter.CTkLabel(w3, text="Agregar referencia")
    mensaje.pack()

    nombre = customtkinter.CTkEntry(w3, placeholder_text="Nombre y Apellido")
    nombre.pack()

    telefono = customtkinter.CTkEntry(w3, placeholder_text="Número de teléfono")
    telefono.pack()

def eliminar_referencia():
    w4 = customtkinter.CTkToplevel()
    w4.configure(background="white")
    w4.title("Eliminar Referencia")
    w4.geometry("400x300")

    mensaje = customtkinter.CTkLabel(w4, text="Eliminar referencia")
    mensaje.pack()

    nombre = customtkinter.CTkEntry(w4, placeholder_text="Nombre y Apellido") #Entrada para ingreso de dato
    nombre.pack()

def actualizar_datos():
    w5 = customtkinter.CTkToplevel()
    w5.configure(background="white")
    w5.title("Actualizar Datos")
    w5.geometry("400x300")

    mensaje = customtkinter.CTkLabel(w5, text="Actualizar datos de asociados")
    mensaje.pack()

    codigo = customtkinter.CTkEntry(w5, placeholder_text="Código del asociado")
    codigo.pack()

    nuevo = customtkinter.CTkEntry(w5, placeholder_text="Nuevos datos")
    nuevo.pack()

def registrar():
    ventana.withdraw()
    w2 = customtkinter.CTkToplevel()
    w2.configure(background="white")
    w2.title("R")
    w2.geometry("650x400")
    mensaje = customtkinter.CTkLabel(w2, text="Codigo")
    mensaje.pack()
    codigo = random.randint(1000, 9999)
    mensaje2 = customtkinter.CTkLabel(w2, text=str(codigo))
    mensaje2.pack()
    entrada1 = customtkinter.CTkEntry(w2,  placeholder_text="Nombre Completo")
    entrada1.pack()
    entrada2 = customtkinter.CTkEntry(w2, placeholder_text="Direccion actual")
    entrada2.pack()
    mensaje5 = customtkinter.CTkLabel(w2, text="Telefonos de contacto:")
    mensaje5.pack()
    entrada3 = customtkinter.CTkEntry(w2, placeholder_text="telefono 1")
    entrada3.pack()
    entrada4 = customtkinter.CTkEntry(w2, placeholder_text="telefono 2")
    entrada4.pack()
    entrada5 = customtkinter.CTkEntry(w2, placeholder_text="Numero DPI")
    entrada5.pack()
    entrada6 = customtkinter.CTkEntry(w2, placeholder_text="NIT")
    entrada6.pack()
    mensaje10 = customtkinter.CTkLabel(w2, text="Referencias personales:")
    mensaje10.pack()
    entrada7 = customtkinter.CTkEntry(w2, placeholder_text="1.Nombre y Apellido")
    entrada7.pack()
    entrada8 = customtkinter.CTkEntry(w2, placeholder_text="1.Numero de telefono")
    entrada8.pack()

    entrada9 = customtkinter.CTkEntry(w2, placeholder_text="2. Nombre y Apellido")
    entrada9.pack()
    entrada10 = customtkinter.CTkEntry(w2, placeholder_text="2. Numero de telefono")
    entrada10.pack()

    global gestion

    boton3 = customtkinter.CTkButton(w2, text="Guardar", command=lambda: guardar_registro(codigo, entrada1.get(), entrada2.get(),
                                                                            entrada3.get(), entrada4.get(), entrada5.get()
                                                                            , entrada6.get(), entrada7.get(), entrada8.get()
                                                                            , entrada9.get(), entrada10.get(), gestion))  # Lambda funcion anonima que permite guardar unicamente cuando se presiona el boton
    boton3.pack()

    boton4 = customtkinter.CTkButton(w2, text="Mostrar", command=mostrar)
    boton4.pack()


# Funcion que guarda el registro
def guardar_registro(codigo, nombre, direccion, tel1, tel2, dpi, nit, ref1, ref1_telf, ref2, ref2_tel, gestion2: List):
    asociado = Asociado(codigo, nombre, direccion, tel1, tel2, dpi, nit, ref1, ref1_telf, ref2, ref2_tel)

    global gestion
    gestion = gestion2

    gestion.append(asociado)


def mostrar():  # funcion que imprime los datos
    h = customtkinter.CTkToplevel()
    h.configure(background="white")
    h.title("DATOS")
    h.geometry("650x400")

    global gestion

    for asociado in gestion:
        texto = (f"Código: {asociado.codigo}, Nombre: {asociado.nombre}, Direccion: {asociado.direccion} "
                      f", Telefonos de contacto: {asociado.tel1} / {asociado.tel2}, DPI: {asociado.dpi}, "
                      f"NIT: {asociado.nit}, Ref1 - Nombre: {asociado.ref1} / Telefono: {asociado.ref1_tel}"
                      f", Ref2 - Nombre: {asociado.ref2} / Telefono: {asociado.ref2_tel}")
        d = customtkinter.CTkLabel(h, text=texto)
        d.pack()
        boton5 = customtkinter.CTkButton(h, text="Salir", command=h.withdraw)
        boton5.pack()


def cargar_archivo():
    archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar Archivo", filetypes=(("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")))

    if archivo:
        # Agregar solo el nombre del archivo a la lista gestion
        gestion.append(archivo.split("/")[-1])
        mostrar_archivo()


def mostrar_archivo():
    ventana.withdraw()
    m = customtkinter.CTkToplevel()
    m.configure(background="white")
    m.title("ARCHIVOS SUBIDOS")
    m.geometry("650x400")

    global gestion

    for archivo in gestion:
        texto = f"Archivo: {archivo}"
        d = customtkinter.CTkLabel(m, text=texto)
        d.pack()


def main_asociado(gestion2: List):
    ventana.title("Gestion de asociados")  # Le pone titulo
    ventana.geometry("400x400")  # dimensiones de la ventana
    ventana.configure(bg="grey")  # se establece color de fondo

    global gestion
    gestion = gestion2

    boton = customtkinter.CTkButton(ventana, text="Nuevos Asociados", command=cerrar_ventana1)
    boton.pack()

    # Abrir Menu
    ventana2.configure(background="white")
    ventana2.title("REGISTRO")
    ventana2.geometry("650x400")
    mensaje = customtkinter.CTkLabel(ventana2, text="Menu")
    mensaje.pack()
    boton1 = customtkinter.CTkButton(ventana2, text="Registrar", command=registrar)  # boton para registrar
    boton1.pack()
    boton2 = customtkinter.CTkButton(ventana2, text="Almacenar", command=cargar_archivo)  # boton para almacenar
    boton2.pack()
    boton3 = customtkinter.CTkButton(ventana2, text="Agregar referencia", command=agregar_referencia)
    boton3.pack()
    boton4 = customtkinter.CTkButton(ventana2, text="Eliminar referencia", command=eliminar_referencia)
    boton4.pack()
    boton5 = customtkinter.CTkButton(ventana2, text="Actualizar datos de sus asociados", command=actualizar_datos)
    boton5.pack()
    boton7 = customtkinter.CTkButton(ventana2, text="Mostrar datos", command=mostrar)
    boton7.pack()

    ventana.mainloop()