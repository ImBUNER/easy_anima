from tkinter import Toplevel, Frame, Label, Button, Entry
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


    # Botones para cambiar de página
    btn1 = Button(topCard, text="Page 2", command=change_page_2)
    btn1.place(x=450, y=960)

    btn2 = Button(topCard, text="Page 1", command=change_page_1)
    btn2.place(x=300, y=960)

    # Etiqueta para decir en qué pagina está el usuario
    info_page_1 = Label(page_1, text='Atributos - pagina 1', bg='#3290F1')
    info_page_1.place(x=20, y=960)
    
    info_page_2 = Label(page_2, text='Transfondo - pagina 2', bg='#3290F1')
    info_page_2.place(x=20, y=960)

    change_page_2()

    # Imagen del personaje
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
        panel.place(x=30, y=50)

    btn_imagen = Button(page_2, text='Seleccionar imagen', command=image)
    btn_imagen.place(x=80, y=10)

    # Seleccionar imagen
    def open_image():
        image_file = filedialog.askopenfilename(title='Selecciona el archivo ".png"')
        return image_file

    
    # PAGINA 2 - Transfondo del personaje -------------------------------------------------
    label_name = Label(page_2, text='Nombre / Apodo', bg='#3290F1').place(x=320, y=30)
    entry_name = Entry(page_2, width=55).place(x=310, y=50)

    label_raza = Label(page_2, text='Raza', bg='#3290F1').place(x=320, y=80)
    entry_raza = Entry(page_2, width=25).place(x=310, y=100)

    label_nephilim = Label(page_2, text='Nephilim', bg='#3290F1').place(x=560, y=80)
    entry_nephilim = Entry(page_2, width=25).place(x=550, y=100)