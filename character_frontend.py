from tkinter import RAISED, Toplevel, Frame, Label, Button, Entry, Text
from PIL import Image, ImageTk
from tkinter import filedialog

import calculator_backend as logic   
    
def card():
    topCard = Toplevel()
    topCard.title('ficha en blanco - Easy Anima')
    topCard.geometry('800x1000')
    topCard.resizable(0, 0)

    # Creamos los frames
    page_1 = Frame(topCard, bg='#3290F1')
    page_2 = Frame(topCard, bg='#3290F1')

    # Funciones que cambia el frame visible
    def change_page_1():
        page_1.pack(fill='both', expand=1)
        page_2.pack_forget()

    def change_page_2():
        page_2.pack(fill='both', expand=1)
        page_1.pack_forget()


    # Buttons to swap page
    btn1 = Button(topCard, text="Page 2", command=change_page_2, cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn1.place(x=410, y=960)

    btn2 = Button(topCard, text="Page 1", command=change_page_1, cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn2.place(x=300, y=960)

    # Info about the current page
    info_page_1 = Label(page_1, text='Atributos - pagina 1', bg='#3290F1')
    info_page_1.place(x=90, y=960)
    
    info_page_2 = Label(page_2, text='Transfondo - pagina 2', bg='#3290F1')
    info_page_2.place(x=90, y=960)

    change_page_2()

    # Character's image
    def image():
        # Elegimos la imagen "x" y la abrimos
        x = open_image()
        img = Image.open(x)

        # Le damos tamaño y usamos filtros para mejor calidad
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
    
        # Creamos el label y la colocamos
        panel = Label(page_2, image = img)
        panel.image = img
        panel.place(x=30, y=52)

    #Button to select the image
    btn_imagen = Button(page_2, text='Seleccionar imagen', command=image, width=28, cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn_imagen.place(x=30, y=10)

    # Seleccionar imagen
    def open_image():
        image_file = filedialog.askopenfilename(title='Selecciona el archivo ".png"')
        return image_file

    
    # PAGE 2 - Character's background -------------------------------------------------

    #Character's data -----------------
    #Row 0
    label_name = Label(page_2, text='Nombre / Apodo', bg='#3290F1').place(x=320, y=12)
    entry_name = Entry(page_2, width=55).place(x=310, y=30)

    #Row 1
    label_race = Label(page_2, text='Raza', bg='#3290F1').place(x=320, y=62)
    entry_race = Entry(page_2, width=25).place(x=310, y=80)

    label_nephilim = Label(page_2, text='Nephilim', bg='#3290F1').place(x=560, y=62)
    entry_nephilim = Entry(page_2, width=25).place(x=550, y=80)

    #Row 2
    label_area = Label(page_2, text='Región', bg='#3290F1').place(x=320, y=112)
    entry_area = Entry(page_2, width=25).place(x=310, y=130)

    label_social = Label(page_2, text='Clase social', bg='#3290F1').place(x=560, y=112)
    entry_social = Entry(page_2, width=25).place(x=550, y=130)

    #Row 3
    label_height = Label(page_2, text='Altura (m)', bg='#3290F1').place(x=320, y=162)
    entry_height = Entry(page_2, width=10).place(x=310, y=180)

    label_weight = Label(page_2, text='Peso (kg)', bg='#3290F1').place(x=440, y=162)
    entry_weight = Entry(page_2, width=10).place(x=430, y=180)

    label_eyes = Label(page_2, text='Ojos', bg='#3290F1').place(x=560, y=162)
    entry_eyes = Entry(page_2, width=10).place(x=550, y=180)

    label_hair = Label(page_2, text='Cabello', bg='#3290F1').place(x=680, y=162)
    entry_hair = Entry(page_2, width=10).place(x=670, y=180)

    #Row 4
    label_gender = Label(page_2, text='Género', bg='#3290F1').place(x=320, y=212)
    entry_gender = Entry(page_2, width=10).place(x=310, y=230)

    label_age = Label(page_2, text='Edad', bg='#3290F1').place(x=440, y=212)
    entry_age = Entry(page_2, width=10).place(x=430, y=230)

    label_skin = Label(page_2, text='Tez', bg='#3290F1').place(x=560, y=212)
    entry_skin = Entry(page_2, width=10).place(x=550, y=230)

    label_ethnic = Label(page_2, text='Etnia', bg='#3290F1').place(x=680, y=212)
    entry_ethnic = Entry(page_2, width=10).place(x=670, y=230)

    #Row 5
    label_experiencie = Label(page_2, text='Experiencia:', bg='#3290F1').place(x=320, y=282)

    label_experiencie_currently = Label(page_2, text='Actual', bg='#3290F1').place(x=440, y=262)
    entry_experiencie_currentlylabel = Entry(page_2, width=10).place(x=430, y=280)

    label_experiencie_total = Label(page_2, text='Total', bg='#3290F1').place(x=560, y=262)
    entry_experiencie_total = Entry(page_2, width=10).place(x=550, y=280)

    label_experiencie_next_level = Label(page_2, text='Sig. nivel', bg='#3290F1').place(x=680, y=262)
    entry_experiencie_next_level = Entry(page_2, width=10).place(x=670, y=280)
    
    
    #Character's personality ----------------
    label_box_personality =Label(page_2, text='Personalidad', bg='#3290F1').place(x=40, y=308)
    box_personality = Text(page_2, bg="white", height=5, width=90).place(x=30, y=330)

    #Character's history --------------------
    label_box_history =Label(page_2, text='Historia', bg='#3290F1').place(x=40, y=438)
    box_history = Text(page_2, bg="white", height=10, width=90).place(x=30, y=460)

    #Character's combat equipment -----------
    label_box_combat_equipment =Label(page_2, text='Equipo de combate', bg='#3290F1').place(x=40, y=658)
    box_combat_equipment = Text(page_2, bg="white", height=15, width=42).place(x=30, y=680)

    #Character's varied equipment ----------
    label_box_varied_equipment =Label(page_2, text='Equipo variado', bg='#3290F1').place(x=420, y=658)
    box_varied_equipment = Text(page_2, bg="white", height=15, width=42).place(x=410, y=680)

    