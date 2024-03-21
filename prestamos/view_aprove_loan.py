import customtkinter
from data_structures.double_list import DoubleList
from tkinter import ttk, messagebox
from tkinter import *
from data_structures.list import List
from prestamos.loan import Loan

'''
Se importaron módulos
tkinter y customtkinter: diseño
estructuras vistas en clase: lista simple
'''

# Global de lista de prestamos e item seleccionado de la tabla
loans = None
item = None

# Función para cargar datos a ventana de CTK
def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Mostrar y aprobar prestamos")
    ventana.geometry('1150x600')
    return ventana


# Creación de función principal donde se cargará todo
def main_window(list_loans: DoubleList):
    ventana = cargar_datos()
    frame = frame1(ventana)
    color = "#3E4446"
    labels_parte1(frame)



    # Función para obtener selección de la tabla
    def get_selection(event):
        # Evento de selección
        y = event.y
        global item
        # Llamada a datos globales
        item = int(my_tree_2.identify_row(y))
        # Item seleccionado
        state_row = data.find_at(item).data[2]
        # Se obtiene el estado a partir del dato seleccionado
        lb_state = customtkinter.CTkLabel(master=frame, text=state_row,
                                          font=("Times New Roman", 20), )
        lb_state.pack(pady=400, padx=400, )
        lb_state.place(x=250, y=50)

        '''
        Se verifica la accesibilidad de botones:
        si el prestamo es aprobado los otros dos botones se activan
        si el prestamo esta en curso, se desactiva aprobado y el mismo
        si el prestamo esta finalizado se desactivan todos los botones
        '''

        if state_row == 'Aprobado':
            bt_finish._state = 'normal'
            bt_process._state = 'normal'
            bt_aproove._state = 'disabled'
        elif state_row == 'En curso':
            bt_finish._state = 'normal'
            bt_aproove._state = 'disabled'
            bt_process._state = 'disabled'
        elif state_row == 'Finalizado':
            bt_finish._state = 'disabled'
            bt_process._state = 'disabled'
            bt_aproove._state = 'disabled'

    # Función para aprovar prestamo
    def aproove():
        if item is None:
            # Si no hay filas seleccionadas
            messagebox.showwarning('Sin selección', 'Debe seleccionar una fila para modificarla')
        else:
            # Si hay una fila seleccionada se aprueba el prestamo de esa fila
            loans.search_by_index(item).data.state_loan = 'Aprobado'
            messagebox.showinfo('Accion finalizada', 'El prestamo ha sido aprobado')
            ventana.destroy()

    # Función para marcar como finalizado
    def end_process():
        if item is None:
            # Si no hay filas seleccionadas
            messagebox.showwarning('Sin selección', 'Debe seleccionar una fila para modificarla')
        else:
            # Si hay una fila seleccionada se finaliza el prestamo de esa fila
            loans.search_by_index(item).data.state_loan = 'Finalizado'
            messagebox.showinfo('Accion finalizada', 'El prestamo ha sido establecido como Finalizado')
            ventana.destroy()

    # Función para poner en proceso
    def process():
        if item is None:
            # Si no hay filas seleccionadas
            messagebox.showwarning('Sin selección', 'Debe seleccionar una fila para modificarla')
        else:
            # Si hay una fila seleccionada se finaliza el prestamo de esa fila
            loans.search_by_index(item).data.state_loan = 'En curso'
            messagebox.showinfo('Accion finalizada', 'El prestamo ha sido establecido como "en curso"')
            ventana.destroy()

    # Se obtiene la lista de main
    global loans
    loans = list_loans

    # Botones con las funciones correspondientes
    bt_aproove = customtkinter.CTkButton(frame, width=440, height=35,
                                         text='Aprobar prestamo', font=("Times New Roman", 20), command=aproove)
    bt_aproove.pack(pady=10, padx=10)
    bt_aproove.place(x=10, y=90)

    bt_process = customtkinter.CTkButton(frame, width=440, height=35, text='Marcar como "En curso"',
                                         font=("Times New Roman", 20), command=process)
    bt_process.pack(pady=10, padx=10)
    bt_process.place(x=10, y=130)

    bt_finish = customtkinter.CTkButton(frame, width=440, height=35, text='Marcar como finalizado',
                                         font=("Times New Roman", 20), fg_color='#5E2129', command=end_process)
    bt_finish.pack(pady=10, padx=10)
    bt_finish.place(x=10, y=170)

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
    tree_frame.place(x=10, y=350)

    # Scrollbar de la tabla
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Creo la tabla

    my_tree_2 = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended', height=50)
    my_tree_2.pack()

    tree_scroll.config(command=my_tree_2.yview)

    my_tree_2['columns'] = ('ID', 'Asociado', 'Estado', 'Monto', 'Cuotas',
                            'Monto aprobado', 'Ingresos', 'Garantía', 'Plan')

    # Columnas de la tabla

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

    # Evento de selección que llama a la función
    my_tree_2.bind("<ButtonRelease-1>", get_selection)

    count = 0

    # Impresión de datos de prestamos en tabla
    data = List()
    for i in loans:
        data.append([i.code_loan, i.code_associate, i.state_loan, i.amount_request,
                     i.nu_dues, i.amount_approved, i.income_associate, i.warranty, i.plan])

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
    # Se crea el frame o columna donde va el diseño
    frame = customtkinter.CTkFrame(master=ventana, height=800)
    frame.pack(pady=10, padx=60, fill='both', ipady=100)
    return frame


def labels_parte1(frame):
    # Labels del diseño
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


