from tkinter import ttk  # En esta parte se importo lo necesario
from tkinter import *
import tkinter
import customtkinter
from data_structures.double_list import DoubleList

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def cambio_datos(listausuario: DoubleList):  # En esta parte se creo la funcion para mostrar la ventana de datos
    visu = customtkinter.CTk()
    visu.title("Cambio datos")
    visu.geometry("800x400")
    lista_usuarios = listausuario

    style = ttk.Style()  # En esta parte se le da estilos a la tabla que se va a crear
    style.theme_use('default')
    style.configure('Treeview',
                    background='#D3D3D3',
                    foreground='black',
                    rowheight=25,
                    fieldbackground='#D3D3D3',
                    font=('Times New Roman', 12))
    style.configure('Treeview.Heading', font=('Times New Roman', 12))

    style.map('Treeview',
              background=[('selected', '#347083')])

    tree_frame = Frame(visu)
    tree_frame.pack(pady=70)
    tree_frame.place(x=10, y=0)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    tabla_visual = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')  # Se crea la tabla
    tabla_visual.pack()

    tree_scroll.config(command=tabla_visual.yview)

    tabla_visual['columns'] = ('Codigo', 'Nombres', 'Correos', 'Contraseñas', 'Puestos', 'Estado')

    tabla_visual.heading('#0', text='', anchor=W)   # Se configuran todos los heading
    tabla_visual.heading('Codigo', text='Codigo', anchor=W)
    tabla_visual.heading('Nombres', text='Nombres', anchor=W)
    tabla_visual.heading('Correos', text='Correos', anchor=W)
    tabla_visual.heading('Contraseñas', text='Contraseñas', anchor=W)
    tabla_visual.heading('Puestos', text='Puestos', anchor=W)
    tabla_visual.heading('Estado', text='Estado', anchor=W)

    tabla_visual.column('#0', anchor=CENTER, width=NO)  # se configuran todos las column
    tabla_visual.column('Codigo', anchor=W, width=50)
    tabla_visual.column('Nombres', anchor=W, width=150)
    tabla_visual.column('Correos', anchor=W, width=150)
    tabla_visual.column('Contraseñas', anchor=W, width=150)
    tabla_visual.column('Puestos', anchor=W, width=150)
    tabla_visual.column('Estado', anchor=W, width=150)

    tabla_visual.tag_configure('oddrow', background='white')
    tabla_visual.tag_configure('evenrow', background='lightblue')

    tabla_visual.delete(*tabla_visual.get_children())

    count = 0
    data = []
    for n in lista_usuarios:  # Para poder pasar la lista a vector
        data.append([n.codigo, n.nombre, n.correo, n.contrasena, n.puesto, n.estado])

    for record in data:  # Para poder visualizar lo que esta en la lista en la tabla
        if count % 2 == 0:
            tabla_visual.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2],
                                                                                    record[3], record[4], record[5]),
                                tags=('evenrow',))
        else:
            tabla_visual.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2],
                                                                                    record[3], record[4], record[5]),
                                tags=('oddrow',))
        count += 1

    codigo = customtkinter.CTkLabel(master=visu, text="Codigo actual")  # En esta parte se crean los Label y Entry
    # para colocar el correo nombre y contraseña en su sitio
    codigo.place(relx=0.15, rely=0.65, anchor=tkinter.CENTER)

    codig = customtkinter.CTkEntry(master=visu)
    codig.place(relx=0.35, rely=0.65, anchor=tkinter.CENTER)

    nombre = customtkinter.CTkLabel(master=visu, text="Nombre")
    nombre.place(relx=0.15, rely=0.75, anchor=tkinter.CENTER)

    cambio_nombre = customtkinter.CTkEntry(master=visu)
    cambio_nombre.place(relx=0.35, rely=0.75, anchor=tkinter.CENTER)

    correo = customtkinter.CTkLabel(master=visu, text="Correo")
    correo.place(relx=0.15, rely=0.85, anchor=tkinter.CENTER)

    cambio_correo = customtkinter.CTkEntry(master=visu)
    cambio_correo.place(relx=0.35, rely=0.85, anchor=tkinter.CENTER)

    puesto = customtkinter.CTkLabel(master=visu, text="Puesto")
    puesto.place(relx=0.15, rely=0.95, anchor=tkinter.CENTER)

    cambio_puesto = customtkinter.CTkEntry(master=visu)
    cambio_puesto.place(relx=0.35, rely=0.95, anchor=tkinter.CENTER)

    def activar():  # Función para hacer los cambios a la lista
        for camb_estado_activo in lista_usuarios:
            if int(camb_estado_activo.codigo) == int(codig.get()):
                camb_estado_activo.nombre = cambio_nombre.get()
                camb_estado_activo.correo = cambio_correo.get()
                camb_estado_activo.puesto = cambio_puesto.get()

    boton_activo = customtkinter.CTkButton(master=visu, text="Cambiar", command=activar)  # Boton para llamar la acción
    boton_activo.place(relx=0.55, rely=0.75, anchor=tkinter.CENTER)

    visu.mainloop()  # Para iniciar la ventana
