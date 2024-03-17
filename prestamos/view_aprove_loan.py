import customtkinter
from tkinter import ttk
from tkinter import *


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Mostrar y aprobar prestamos")
    ventana.geometry('1150x600')
    return ventana


def main_window():
    ventana = cargar_datos()
    frame = frame1(ventana)
    color = "#3E4446"
    labels_parte1(frame)

    tb_state = customtkinter.CTkEntry(master=frame, font=("Times New Roman", 20), width=200,
                                      placeholder_text='', state='disabled')
    tb_state.pack(pady=400, padx=400, )
    tb_state.place(x=250, y=50)

    bt_aproove = customtkinter.CTkButton(frame, width=440, height=35, text='Aprobar prestamo', font=("Times New Roman", 20))
    bt_aproove.pack(pady=10, padx=10)
    bt_aproove.place(x=10, y=90)

    bt_process = customtkinter.CTkButton(frame, width=440, height=35, text='Marcar como "En curso"',
                                         font=("Times New Roman", 20))
    bt_process.pack(pady=10, padx=10)
    bt_process.place(x=10, y=130)

    bt_finish = customtkinter.CTkButton(frame, width=440, height=35, text='Marcar como finalizado',
                                         font=("Times New Roman", 20), fg_color='#5E2129')
    bt_finish.pack(pady=10, padx=10)
    bt_finish.place(x=10, y=170)

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
    tree_frame.place(x=10, y=350)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree_2 = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended', height=50)
    my_tree_2.pack()

    tree_scroll.config(command=my_tree_2.yview)

    my_tree_2['columns'] = ('ID', 'Asociado', 'Estado', 'Monto', 'Cuotas',
                            'Monto aprobado', 'Ingresos', 'Garantía', 'Plan')

    my_tree_2.column('#0', width=0, stretch=NO)
    my_tree_2.column('ID', anchor=W, stretch=NO)
    my_tree_2.column('Asociado', anchor=W)
    my_tree_2.column('Estado', anchor=W, stretch=NO, width=120)
    my_tree_2.column('Monto', anchor=W, stretch=NO, width=120)
    my_tree_2.column('Cuotas', anchor=W, stretch=NO, width=120)
    my_tree_2.column('Monto aprobado', anchor=W, stretch=NO, width=120)
    my_tree_2.column('Ingresos', anchor=W, stretch=NO, width=120)
    my_tree_2.column('Garantía', anchor=W, stretch=NO, width=120)
    my_tree_2.column('Plan', anchor=W, stretch=NO, width=120)

    my_tree_2.heading('#0', text='', anchor=W)
    my_tree_2.heading('ID', text='ID', anchor=W)
    my_tree_2.heading('Asociado', text='Asociado', anchor=W)
    my_tree_2.heading('Estado', text='Estado', anchor=W)
    my_tree_2.heading('Monto', text='Monto', anchor=W)
    my_tree_2.heading('Cuotas', text='Cuotas', anchor=W)
    my_tree_2.heading('Monto aprobado', text='Monto aprobado', anchor=W)
    my_tree_2.heading('Ingresos', text='Ingresos', anchor=W)
    my_tree_2.heading('Garantía', text='Garantía', anchor=W)
    my_tree_2.heading('Plan', text='Plan', anchor=W)

    my_tree_2.tag_configure('oddrow', background='white')
    my_tree_2.tag_configure('evenrow', background='lightblue')

    count = 0

    data = []

    for record in data:
        if count % 2 == 0:
            my_tree_2.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3],
                                   record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
        else:
            my_tree_2.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3],
                                   record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
        count += 1


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana, height=800)
    frame.pack(pady=10, padx=60, fill='both', ipady=100)
    return frame


def labels_parte1(frame):
    lb_title = customtkinter.CTkLabel(master=frame, text='Visualizar y verificar prestamos',
                                      font=("Times New Roman", 30, "bold"))
    lb_title.pack(pady=400, padx=400, )
    lb_title.place(x=300, y=0)

    lb_state = customtkinter.CTkLabel(master=frame, text='Estado actual del prestamo: ',
                                      font=("Times New Roman", 20))
    lb_state.pack(pady=400, padx=400, )
    lb_state.place(x=10, y=50)

    lb_loan_code = customtkinter.CTkLabel(master=frame, text='Lista de prestamos '
                                                             '(seleccione una fila para realizar cambios)',
                                          font=("Times New Roman", 20))
    lb_loan_code.pack(pady=400, padx=400, )
    lb_loan_code.place(x=10, y=240)


