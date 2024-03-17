import customtkinter
from prestamos import pay_loan
from prestamos import request_loan
from prestamos import view_aprove_loan

root = customtkinter.CTk()


def open_view():
    view_aprove_loan.main_window()


def open_pay():
    pay_loan.main_window()


def open_request():
    request_loan.main_window()


def buttons(frame, frame2):

    button_1 = customtkinter.CTkButton(master=frame, text='Solicitar prestamo bancario', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446", command=open_request)
    button_2 = customtkinter.CTkButton(master=frame2, text='Visualizar y aprobar prestamos', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446", command=open_view)

    button_4 = customtkinter.CTkButton(master=frame, text='Realizar pagos', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446", command=open_pay)

    button_1.pack(pady=34, padx=10)
    button_2.pack(pady=34, padx=10)
    button_4.pack(pady=34, padx=10)

    return


def main_window():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root.title("Menú de Prestamos Bancarios")
    frame = customtkinter.CTkFrame(master=root)
    root.wm_attributes("-topmost", False)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    frame2 = customtkinter.CTkFrame(master=frame, fg_color="#212121", width=50)
    frame2.pack(pady=10, padx=8, fill='both', expand=True, side='right')
    frame3 = customtkinter.CTkFrame(master=frame, fg_color="#212121")
    frame3.pack(pady=20, padx=8, fill='both', expand=True, side='left')

    buttons(frame3, frame2)

    frame.pack()
    root.geometry('800x450')
    root.mainloop()
