from tkinter import ttk, messagebox
from tkinter import *
import customtkinter
from data_structures.double_list import DoubleList
from data_structures.circular_list import CircularList
from CTkListbox import *

'''
Se importaron módulos
tkinter y customtkinter: diseño
estructuras vistas en clase: doble lista, lista circular
listbox: parte del diseño
'''

# Datos globales: prestamos, elemento seleccionado, total aprovado, total de pagos, historial de pagos
loans = None
item = None
aprooved_total = 0
total = 0
pay_history = None


# Función para cargar datos a ventana de CTK
def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Solicitar prestamo")
    ventana.geometry('920x375')
    return ventana


# Creación de función principal donde se cargará todo
def main_window(loan_list: DoubleList):
    ventana = cargar_datos()
    frame = frame1(ventana)
    color = "#3E4446"
    labels_parte1(frame)

    global loans
    loans = loan_list
    # Se obtiene la lista de main

    # Función para obtener selección de la tabla
    def get_selection(event):
        # Evento de selección
        y = event.y
        listbox_history.delete(0, 'END')
        global item
        global total
        total = 0
        global pay_history
        # Llamada a datos globales
        item = int(my_tree.identify_row(y))
        # Historial de pago
        pay_history = data.find_at(item).data[4]
        for j in pay_history:
            total += j
            listbox_history.insert('END', 'Q ' + str(j))
            # Se concatenan datos a la listbox y al total
        global aprooved_total
        # Total aprobado
        aprooved_total = data.find_at(item).data[5]

        # Labels (texto) que se modifica entre el programa
        lb_total_pay = customtkinter.CTkLabel(master=frame, text='Q ' + str(total), font=("Times New Roman", 20))
        lb_total_pay.pack(pady=400, padx=400, )
        lb_total_pay.place(x=580, y=280)

        lb_aprooved = customtkinter.CTkLabel(master=frame, text='Q ' + str(aprooved_total), font=("Times New Roman", 20))
        lb_aprooved.pack(pady=400, padx=400, )
        lb_aprooved.place(x=580, y=310)

        # Estado del boton de subir total si el total puede ser modificado o ya no
        if total == aprooved_total:
            bt_cargar._state = 'disabled'
        else:
            bt_cargar._state = 'normal'

    # Función para pagar un monto en específico
    def pagar():
        # Se obtiene el total del exterior
        global total
        if item is None:
            messagebox.showwarning('Sin selección', 'Debe seleccionar una fila para modificarla')
            # evento si no hay selección
        else:
            # Si el pago se puede hacer
            pago = int(ib_monto.get())
            if total + pago > aprooved_total:
                # El pago es mayor al total aprobado
                messagebox.showwarning('Pago incorrecto', 'No se debe pagar mas dinero del aprobado')
            elif total + pago == aprooved_total:
                # El pago ya llegó a su límite
                pay_history.append(pago)
                total += pago
                # Se añade el pago a la listbox
                listbox_history.insert('END', 'Q ' + str(pago))
                messagebox.showwarning('Pago finalizado', 'El préstamo se ha pagado correctamente')
            else:
                total += pago
                pay_history.append(pago)
                listbox_history.insert('END', 'Q ' + str(pago))
            # Si hay pago, se añade a las labels
            lb_total_pay = customtkinter.CTkLabel(master=frame, text='Q ' + str(total), font=("Times New Roman", 20))
            lb_total_pay.pack(pady=400, padx=400, )
            lb_total_pay.place(x=580, y=280)

    # Elementos gráficos (labels: texto, bt: botones)
    ib_monto = customtkinter.CTkEntry(master=frame, placeholder_text='Monto de pago',
                                         width=100)
    ib_monto.pack(pady=100, padx=10)
    ib_monto.place(x=540, y=60)

    bt_cargar = customtkinter.CTkButton(frame, width=100, height=35, text='Cargar pago', font=("Times New Roman", 15), command=pagar)
    bt_cargar.pack(pady=10, padx=10)
    bt_cargar.place(x=650, y=55)

    listbox_history = CTkListbox(frame, width=270)
    listbox_history.pack(fill='both', expand=True, padx=10, pady=10)
    listbox_history.place(y=150, x=400)

    # Estilo de la tabla
    style = ttk.Style()
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

    tree_frame = Frame(frame)
    tree_frame.pack(pady=70)
    tree_frame.place(x=10, y=140)

    # Scrollbar de la tabla
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Creo la tabla
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ('ID', 'Asociado', 'Monto', 'Estado')

    # Columnas de la tabla
    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('ID', anchor=W, width=50)
    my_tree.column('Asociado', anchor=W, width=125)
    my_tree.column('Monto', anchor=W, width=125)
    my_tree.column('Estado', anchor=W, width=125)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('ID', text='ID', anchor=W)
    my_tree.heading('Asociado', text='Asociado', anchor=W)
    my_tree.heading('Monto', text='Monto solicitado', anchor=W)
    my_tree.heading('Estado', text='Estado', anchor=W)

    my_tree.tag_configure('oddrow', background='white')
    my_tree.tag_configure('evenrow', background='lightblue')

    # Evento de selección que llama a la función
    my_tree.bind("<ButtonRelease-1>", get_selection)

    count = 0

    # Impresión de datos de prestamos en tabla
    data = CircularList()
    for i in loans:
        data.append([i.code_loan, i.code_associate, i.amount_request, i.state_loan, i.historial, i.amount_approved])

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                             values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                             values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        count += 1


def frame1(ventana):
    # Se crea el frame o columna donde va el diseño
    frame = customtkinter.CTkFrame(master=ventana, height=800)
    frame.pack(pady=10, padx=60, fill='both', ipady=100)
    return frame


def labels_parte1(frame):
    # Labels del diseño
    lb_title = customtkinter.CTkLabel(master=frame, text='Pagar prestamos',
                                      font=("Times New Roman", 30, "bold"))
    lb_title.pack(pady=400, padx=400, )
    lb_title.place(x=300, y=0)

    lb_list = customtkinter.CTkLabel(master=frame, text='Lista de prestamos: ', font=("Times New Roman", 20))
    lb_list.pack(pady=400, padx=400, )
    lb_list.place(x=10, y=60)

    lb_monto = customtkinter.CTkLabel(master=frame, text='Monto de pago:', font=("Times New Roman", 20))
    lb_monto.pack(pady=400, padx=400, )
    lb_monto.place(x=400, y=60)

    lb_monto = customtkinter.CTkLabel(master=frame, text='Historial de pagos: ', font=("Times New Roman", 20))
    lb_monto.pack(pady=400, padx=400, )
    lb_monto.place(x=400, y=110)

    lb_total_pagado = customtkinter.CTkLabel(master=frame, text='Total pagado: ', font=("Times New Roman", 20))
    lb_total_pagado.pack(pady=400, padx=400, )
    lb_total_pagado.place(x=400, y=280)

    lb_monto_aprobado = customtkinter.CTkLabel(master=frame, text='Monto aprobado: ', font=("Times New Roman", 20))
    lb_monto_aprobado.pack(pady=400, padx=400, )
    lb_monto_aprobado.place(x=400, y=310)
