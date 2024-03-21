from tkinter import ttk  # En esta parte se importo lo necesario
from tkinter import *
import customtkinter
from listadobleenlace import List

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def visualizar(listausuario: List):  # En esta parte se creo la funcion para mostrar la ventana de vizualizar
    visu = customtkinter.CTk()
    visu.title("Regristro de usuarios")
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

    tabla_visual = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')   # Se crea la tabla
    tabla_visual.pack()

    tree_scroll.config(command=tabla_visual.yview)

    tabla_visual['columns'] = ('Codigo', 'Nombres', 'Correos', 'Contraseñas', 'Puestos', 'Estado')

    tabla_visual.heading('#0', text='', anchor=W)  # Se configuran todos los heading
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
    for n in lista_usuarios:   # Para poder pasar la lista a vector
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

    visu.mainloop()  # Para iniciar la ventana

