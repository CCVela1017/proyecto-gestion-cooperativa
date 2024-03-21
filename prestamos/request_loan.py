import customtkinter
import random
from CTkListbox import *
from tkinter import messagebox
from prestamos.loan import Loan
from data_structures.double_list import DoubleList
from data_structures.list import List

loans = None

def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Solicitar prestamo")
    ventana.geometry('1000x450')
    return ventana


def main_window(list_prestamos: DoubleList):
    ventana = cargar_datos()
    frame = frame1(ventana)
    color = "#3E4446"
    labels_parte1(frame)

    global loans
    loans = list_prestamos

    files = List()

    code_ln = str(random.randint(1, 5000))

    def obtener_archivo():
        text = ib_file_name.get()
        listbox_files.insert('END', text)
        files.append(text)

    def create_loan():
        associate_code = ib_associate_code.get()
        amount = ib_amount.get()
        fee_num = ib_fee_num.get()
        income = ib_monthly_income.get()
        garantia = ib_warranty.get()
        plan = ib_pay_plan.get()

        if associate_code == '' or amount == '' or fee_num == '' or income == '' or garantia == '' or plan == '':
            messagebox.showwarning('Sin ingreso', 'Algunas de las casillas estan en blanco')
        else:
            new_loan = Loan(code_ln, associate_code, int(amount), int(fee_num), 'Creado',
                            int(income), garantia, files, plan)
            loans.append(new_loan)
            ventana.destroy()
            messagebox.showinfo('Datos ingresados', 'Todos los datos del prestamo se ingresaron correctamente')

    lb_loan_code2 = customtkinter.CTkLabel(master=frame, font=("Times New Roman", 20), text=code_ln)
    lb_loan_code2.pack(pady=400, padx=400, )
    lb_loan_code2.place(x=200, y=60)

    ib_associate_code = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese el código del asociado',
                                               width=200, height=35)
    ib_associate_code.pack(pady=100, padx=10)
    ib_associate_code.place(x=525, y=60)

    ib_monthly_income = customtkinter.CTkEntry(master=frame, placeholder_text='Ingresos mensuales',
                                           width=215, height=35)
    ib_monthly_income.pack(pady=100, padx=10)
    ib_monthly_income.place(x=625, y=110)

    ib_amount = customtkinter.CTkEntry(master=frame, placeholder_text='Ingreso Monto')
    ib_amount.pack(pady=75, padx=10)
    ib_amount.place(x=185, y=110)

    ib_fee_num = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese No. Cuotas', width=130, height=35)
    ib_fee_num.pack(pady=100, padx=10)
    ib_fee_num.place(x=185, y=160)

    ib_warranty = customtkinter.CTkEntry(master=frame, placeholder_text='Garantía',
                                         width=100)
    ib_warranty.pack(pady=100, padx=10)
    ib_warranty.place(x=600, y=160)

    ib_pay_plan = CTkListbox(frame, width=115)
    ib_pay_plan.pack(fill='both', expand=True, padx=10, pady=10)
    ib_pay_plan.place(x=185, y=210)
    ib_pay_plan.insert(0, "6 Meses")
    ib_pay_plan.insert(1, "12 Meses")
    ib_pay_plan.insert(2, "18 Meses")
    ib_pay_plan.insert(3, "24 Meses")
    ib_pay_plan.insert('END', "36 Meses")

    ib_file_name = customtkinter.CTkEntry(master=frame, placeholder_text='Nombre del archivo',
                                          width=160)
    ib_file_name.pack(pady=100, padx=10)
    ib_file_name.place(x=510, y=210)

    listbox_files = CTkListbox(frame, width=270)
    listbox_files.pack(fill='both', expand=True, padx=10, pady=10)
    listbox_files.place(y=250, x=510)

    bt_crear = customtkinter.CTkButton(frame, width=490, height=35, text='Crear Prestamo',
                                       font=("Times New Roman", 20), command=create_loan)
    bt_crear.pack(pady=10, padx=10)
    bt_crear.place(x=10, y=350)

    boton_add2 = customtkinter.CTkButton(master=frame, text='+', font=("Times New Roman", 40, "bold"), width=55, command=obtener_archivo)
    boton_add2.pack(pady=400, padx=400)
    boton_add2.place(x=815, y=250)

    return loans

def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana, height=800)
    frame.pack(pady=10, padx=60, fill='both', ipady=100)
    return frame


def labels_parte1(frame):
    lb_title = customtkinter.CTkLabel(master=frame, text='Solicitar Préstamo',
                                      font=("Times New Roman", 30, "bold"))
    lb_title.pack(pady=400, padx=400, )
    lb_title.place(x=300, y=0)

    lb_loan_code = customtkinter.CTkLabel(master=frame, text='Código de prestamo: ', font=("Times New Roman", 20))
    lb_loan_code.pack(pady=400, padx=400, )
    lb_loan_code.place(x=10, y=60)

    lb_associate_code = customtkinter.CTkLabel(master=frame, text='Código del asociado: ', font=("Times New Roman", 20))
    lb_associate_code.pack(pady=400, padx=400)
    lb_associate_code.place(x=350, y=60)

    lb_amount = customtkinter.CTkLabel(master=frame, text='Monto solicitado: ', font=("Times New Roman", 20))
    lb_amount.pack(pady=400, padx=400)
    lb_amount.place(x=10, y=110)

    lb_fee_num = customtkinter.CTkLabel(master=frame, text='Número de cuotas: ', font=("Times New Roman", 20))
    lb_fee_num.pack(pady=400, padx=400)
    lb_fee_num.place(x=10, y=160)

    lb_monthly_income = customtkinter.CTkLabel(master=frame, text='Ingresos mensuales del asociado: ', font=("Times New Roman", 20))
    lb_monthly_income.pack(pady=400, padx=400)
    lb_monthly_income.place(x=350, y=110)

    # label 2

    lb_warranty = customtkinter.CTkLabel(master=frame, text='Garantía que deja el asociado: ', font=("Times New Roman", 20))
    lb_warranty.pack(pady=400, padx=400)
    lb_warranty.place(x=350, y=160)

    lb_files = customtkinter.CTkLabel(master=frame, text='Archivos adjuntos: ', font=("Times New Roman", 20))
    lb_files.pack(pady=400, padx=400)
    lb_files.place(x=350, y=210)

    lb_pay_plan = customtkinter.CTkLabel(master=frame, text='Plan de pagos: ',
                                                    font=("Times New Roman", 20))
    lb_pay_plan.pack(pady=400, padx=400)
    lb_pay_plan.place(x=10, y=210)

