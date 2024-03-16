import customtkinter
import random
from CTkListbox import *


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Solicitar prestamo")
    ventana.geometry('1000x400')
    return ventana


def main_window():
    ventana = cargar_datos()
    frame = frame1(ventana)
    color = "#3E4446"
    labels_parte1(frame)

    code = random.randint(1, 1000)

    ib_loan_code = customtkinter.CTkEntry(master=frame, width=150, height=35,
                                          state='disabled', placeholder_text=str(code))
    ib_loan_code.pack(pady=12, padx=10)
    ib_loan_code.place(x=185, y=60)

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

    ib_pay_plan = customtkinter.CTkEntry(master=frame, placeholder_text='Plan de pago', width=180, height=35)
    ib_pay_plan.pack(pady=100, padx=10)
    ib_pay_plan.place(x=150, y=210)

    listbox_files = CTkListbox(frame, width=270)
    listbox_files.pack(fill='both', expand=True, padx=10, pady=10)
    listbox_files.place(y=210, x=510)

    listbox_files.insert(0, "Option 0")
    listbox_files.insert(1, "Option 1")
    listbox_files.insert(2, "Option 2")
    listbox_files.insert('END', "Option 3")

    bt_crear = customtkinter.CTkButton(frame, width=490, height=35, text='Crear Prestamo', font=("Times New Roman", 20))
    bt_crear.pack(pady=10, padx=10)
    bt_crear.place(x=10, y=300)

    boton_add2 = customtkinter.CTkButton(master=frame, text='+', font=("Times New Roman", 40, "bold"), width=55)
    boton_add2.pack(pady=400, padx=400)
    boton_add2.place(x=815, y=210)




def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana, height=800)
    frame.pack(pady=10, padx=60, fill='both', ipady=100)
    return frame


def labels_parte1(frame):
    lb_title = customtkinter.CTkLabel(master=frame, text='Solicitar prestamo',
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

