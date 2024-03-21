from tkinter import ttk
from tkinter import *
import customtkinter
from data_structures.double_list import DoubleList
import random
from CTkListbox import *

loans = None

def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Solicitar prestamo")
    ventana.geometry('920x375')
    return ventana


def main_window(loan_list: DoubleList):
    ventana = cargar_datos()
    frame = frame1(ventana)
    color = "#3E4446"
    labels_parte1(frame)

    global loans
    loans = loan_list

    ib_monto = customtkinter.CTkEntry(master=frame, placeholder_text='Monto de pago',
                                         width=100)
    ib_monto.pack(pady=100, padx=10)
    ib_monto.place(x=540, y=60)

    bt_crear = customtkinter.CTkButton(frame, width=100, height=35, text='Cargar pago', font=("Times New Roman", 15))
    bt_crear.pack(pady=10, padx=10)
    bt_crear.place(x=650, y=55)

    listbox_history = CTkListbox(frame, width=270)
    listbox_history.pack(fill='both', expand=True, padx=10, pady=10)
    listbox_history.place(y=150, x=400)

    listbox_history.insert(0, "Option 0")
    listbox_history.insert(1, "Option 1")
    listbox_history.insert(2, "Option 2")
    listbox_history.insert('END', "Option 3")

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

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ('ID', 'Asociado', 'Monto', 'Estado')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('ID', anchor=W, width=50)
    my_tree.column('Asociado', anchor=W, width=125)
    my_tree.column('Monto', anchor=W, width=125)
    my_tree.column('Estado', anchor=W, width=125)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('ID', text='ID', anchor=W)
    my_tree.heading('Asociado', text='Asociado', anchor=W)
    my_tree.heading('Monto', text='Monto', anchor=W)
    my_tree.heading('Estado', text='Estado', anchor=W)

    my_tree.tag_configure('oddrow', background='white')
    my_tree.tag_configure('evenrow', background='lightblue')



def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana, height=800)
    frame.pack(pady=10, padx=60, fill='both', ipady=100)
    return frame


def labels_parte1(frame):
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
