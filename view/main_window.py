from tkinter import Tk, Frame, Label, Button
from PIL import Image, ImageTk
import view.dice_window, view.calculator_window, view.character_window

class app:
    def __init__(self, root):
        self = root
        self.title("main menu - Easy Anima")
        self.geometry("750x510")
        self.resizable(0, 0)
        self.configure(bg="black")

        # Default configuration for app font
        # default_font = font.nametofont("TkDefaultFont")
        # default_font.configure(weight="bold")

        # App logo
        logo = Image.open("static/logo_app.png")
        logo = logo.resize((650, 520), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(image=logo, bg="black")
        logo_label.image = logo
        logo_label.grid(column=1, row=0)

        # Lateral menu
        menu_root = Frame(self, bg="#3290F1")
        menu_root.grid(row=0, column=0, sticky="ns")

        # Menu buttons
        btn_create = Button(
            menu_root,
            text="Nueva Ficha",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=view.character_window.open,
        )
        btn_create.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

        btn_calc = Button(
            menu_root,
            text="Calc. Combate",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=view.calculator_window.open, 
        )
        btn_calc.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

        btn_dice = Button(
            menu_root,
            text="Dados",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=view.dice_window.open,
        )
        btn_dice.grid(row=2, column=0, sticky="ew", padx=20, pady=10)


# I'm BUNER
# if __name__ == "__main__":
#     root = Tk()
#     application = app(root)
#     root.mainloop()
