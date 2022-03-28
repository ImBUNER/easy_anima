from tkinter import Tk, Frame, Label, Button
from PIL import Image, ImageTk
import dices, calculator_frontend, character_frontend

class app:
     def __init__(self, root):
        self = root
        self.title('main menu - Easy Anima')
        self.geometry('750x510')
        self.resizable(0, 0)
        self.configure(bg='black')

        # Logo de la app
        logo = Image.open("static/logo_app.png")
        logo = logo.resize((650, 520), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(image=logo, bg='black')
        logo_label.image = logo
        logo_label.grid(column=1, row=0)

        #Menú lateral
        menu_root = Frame(self, bg='#3290F1')
        menu_root.grid(row=0, column=0, sticky="ns")

        # Botones del menú
        btn_create = Button(menu_root, text='Nueva Ficha', cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', command=character_frontend.card)
        btn_create.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

        btn_calc = Button(menu_root, text='Calc. Combate', cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', command=calculator_frontend.calc)
        btn_calc.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

        btn_dice = Button(menu_root, text='Dados', cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', command=dices.roll)
        btn_dice.grid(row=2, column=0, sticky="ew", padx=20, pady=10)

# I'm BUNER
if __name__ == '__main__':
    root = Tk()
    application = app(root)
    root.mainloop()