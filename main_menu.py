import customtkinter
import prestamos_bancarios
from prestamos.loan import Loan
from data_structures.double_list import DoubleList
from data_structures.list import List
from usuarios_p.class_usuario import Usuarios
from usuarios import main_user
from asociados.asociado import Asociado
from asociados.gestion_asociado import main_asociado
root = customtkinter.CTk()

loans = DoubleList[Loan]()
users = DoubleList[Usuarios]()
asociados = List[Asociado]()


def open_prestamos():
    global loans
    prestamos_bancarios.main_window(loans)


def open_users():
    global users
    main_user(users)


def open_asociados():
    global asociados
    main_asociado(asociados)


def buttons(frame, frame2):

    button_1 = customtkinter.CTkButton(master=frame, text='Gestion de asociados', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446", command=open_asociados)
    button_2 = customtkinter.CTkButton(master=frame2, text='Prestamos bancarios', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446", command=open_prestamos)

    button_4 = customtkinter.CTkButton(master=frame, text='Usuarios', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446", command=open_users)

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


main_window()

