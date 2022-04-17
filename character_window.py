from tkinter import CENTER, NE, RIDGE, Toplevel, Frame, Label, Button, Entry, Text
from tkinter.ttk import Separator
from PIL import Image, ImageTk
from tkinter import filedialog

def open():
    topCard = Toplevel()
    topCard.title('ficha en blanco - Easy Anima')
    topCard.geometry('800x1000')
    topCard.resizable(0, 0)

    # Page frame
    page_1 = Frame(topCard, bg='#3290F1')
    page_2 = Frame(topCard, bg='#3290F1')

    # Function that shows the page and hides the other
    def change_page_1():
        page_1.pack(fill='both', expand=1)
        page_2.pack_forget()

    def change_page_2():
        page_2.pack(fill='both', expand=1)
        page_1.pack_forget()


    # Page change buttons
    btn1 = Button(topCard, text="Page 2", command=change_page_2, cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn1.place(x=410, y=960)

    btn2 = Button(topCard, text="Page 1", command=change_page_1, cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn2.place(x=305, y=960)

    # Info about the current page
    info_page_1 = Label(page_1, text='Atributos - pagina 1', bg='#3290F1')
    info_page_1.place(x=90, y=960)
    
    info_page_2 = Label(page_2, text='Transfondo - pagina 2', bg='#3290F1')
    info_page_2.place(x=90, y=960)

    # Default page
    change_page_1()

    # Character image
    def image():
        # Choose and open the image
        x = open_image()
        img = Image.open(x)

        # Resize and filter the image
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
    
        # Image label
        panel = Label(page_2, image = img)
        panel.image = img
        panel.place(x=30, y=52)

    # Image button
    btn_imagen = Button(page_2, text='Imagen', command=image, width=28, cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn_imagen.place(x=30, y=10)

    # Function to select the image
    def open_image():
        image_file = filedialog.askopenfilename(title='Selecciona un archivo ".png"')
        return image_file

    



    # PAGE 2 - Character background ----------------------------------------------------------

    #Character data -----------------
    #Row 0
    label_name = Label(page_2, text='Nombre / Apodo', bg='#3290F1').place(x=320, y=12)
    entry_name = Entry(page_2, width=55, bg="#f2f2f2").place(x=310, y=30)

    #Row 1
    label_race = Label(page_2, text='Raza', bg='#3290F1').place(x=320, y=62)
    entry_race = Entry(page_2, width=25, bg="#f2f2f2").place(x=310, y=80)

    label_nephilim = Label(page_2, text='Nephilim', bg='#3290F1').place(x=560, y=62)
    entry_nephilim = Entry(page_2, width=25, bg="#f2f2f2").place(x=550, y=80)

    #Row 2
    label_area = Label(page_2, text='Región', bg='#3290F1').place(x=320, y=112)
    entry_area = Entry(page_2, width=25, bg="#f2f2f2").place(x=310, y=130)

    label_social = Label(page_2, text='Clase social', bg='#3290F1').place(x=560, y=112)
    entry_social = Entry(page_2, width=25, bg="#f2f2f2").place(x=550, y=130)

    #Row 3
    label_height = Label(page_2, text='Altura (m)', bg='#3290F1').place(x=320, y=162)
    entry_height = Entry(page_2, width=10, bg="#f2f2f2").place(x=310, y=180)

    label_weight = Label(page_2, text='Peso (kg)', bg='#3290F1').place(x=440, y=162)
    entry_weight = Entry(page_2, width=10, bg="#f2f2f2").place(x=430, y=180)

    label_eyes = Label(page_2, text='Ojos', bg='#3290F1').place(x=560, y=162)
    entry_eyes = Entry(page_2, width=10, bg="#f2f2f2").place(x=550, y=180)

    label_hair = Label(page_2, text='Cabello', bg='#3290F1').place(x=680, y=162)
    entry_hair = Entry(page_2, width=10, bg="#f2f2f2").place(x=670, y=180)

    #Row 4
    label_gender = Label(page_2, text='Género', bg='#3290F1').place(x=320, y=212)
    entry_gender = Entry(page_2, width=10, bg="#f2f2f2").place(x=310, y=230)

    label_age = Label(page_2, text='Edad', bg='#3290F1').place(x=440, y=212)
    entry_age = Entry(page_2, width=10, bg="#f2f2f2").place(x=430, y=230)

    label_skin = Label(page_2, text='Tez', bg='#3290F1').place(x=560, y=212)
    entry_skin = Entry(page_2, width=10, bg="#f2f2f2").place(x=550, y=230)

    label_ethnic = Label(page_2, text='Etnia', bg='#3290F1').place(x=680, y=212)
    entry_ethnic = Entry(page_2, width=10, bg="#f2f2f2").place(x=670, y=230)

    #Row 5
    label_experiencie = Label(page_2, text='Experiencia:', bg='#3290F1').place(x=320, y=282)

    label_experiencie_currently = Label(page_2, text='Actual', bg='#3290F1').place(x=440, y=262)
    entry_experiencie_currentlylabel = Entry(page_2, width=10, bg="#f2f2f2").place(x=430, y=280)

    label_experiencie_total = Label(page_2, text='Total', bg='#3290F1').place(x=560, y=262)
    entry_experiencie_total = Entry(page_2, width=10, bg="#f2f2f2").place(x=550, y=280)

    label_experiencie_next_level = Label(page_2, text='Sig. nivel', bg='#3290F1').place(x=680, y=262)
    entry_experiencie_next_level = Entry(page_2, width=10, bg="#f2f2f2").place(x=670, y=280)
    
    
    #Character personality ----------------
    label_box_personality =Label(page_2, text='Personalidad', bg='#3290F1').place(x=40, y=308)
    box_personality = Text(page_2, bg="#f2f2f2", height=5, width=90).place(x=30, y=330)

    #Character history --------------------
    label_box_history =Label(page_2, text='Historia', bg='#3290F1').place(x=40, y=438)
    box_history = Text(page_2, bg="#f2f2f2", height=10, width=90).place(x=30, y=460)

    #Character combat equipment -----------
    label_box_combat_equipment =Label(page_2, text='Equipo de combate', bg='#3290F1').place(x=40, y=658)
    box_combat_equipment = Text(page_2, bg="#f2f2f2", height=15, width=42).place(x=30, y=680)

    #Character varied equipment ----------
    label_box_varied_equipment =Label(page_2, text='Equipo variado', bg='#3290F1').place(x=420, y=658)
    box_varied_equipment = Text(page_2, bg="#f2f2f2", height=15, width=42).place(x=410, y=680)



    

    # PAGE 1 - Character characteristic -----------------------------------------------------------

    # Character stats ---------------------
    label_stats = Label(page_1, text='Características', bg='#3290F1', font='bold').place(x=70, y=8)
    stats_zone = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="140", width="220").place(x=20, y=30)

    # Column 1
    label_AGI = Label(page_1, text='AGI', bg='#3290F1').place(anchor=NE, x=60, y=42)
    entry_AGI = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=65, y=40)

    label_CON = Label(page_1, text='CON', bg='#3290F1').place(anchor=NE, x=60, y=72)
    entry_CON = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=65, y=70)

    label_DES = Label(page_1, text='DES', bg='#3290F1').place(anchor=NE, x=60, y=102)
    entry_DES = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=65, y=100)

    label_FUE = Label(page_1, text='FUE', bg='#3290F1').place(anchor=NE, x=60, y=132)
    entry_FUE = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=65, y=130)

    # Column 2
    label_INT = Label(page_1, text='INT', bg='#3290F1').place(anchor=NE, x=170, y=42)
    entry_INT = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=175, y=40)

    label_PER = Label(page_1, text='PER', bg='#3290F1').place(anchor=NE, x=170, y=72)
    entry_PER = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=175, y=70)

    label_POD = Label(page_1, text='POD', bg='#3290F1').place(anchor=NE, x=170, y=102)
    entry_POD = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=175, y=100)

    label_VOL = Label(page_1, text='VOL', bg='#3290F1').place(anchor=NE, x=170, y=132)
    entry_VOL = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=175, y=130)



    # Secondary skills
    label_secondary = Label(page_1, text='Habilidades Secundarias', bg='#3290F1', font='bold').place(x=580, y=8)
    secondary_zone = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="950", width="170").place(x=610, y=30)

    # Athletic
    label_acrobatics = Label(page_1, text='Acrobacias', bg='#3290F1').place(anchor=NE, x=700, y=40)
    entry_acrobatics = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=40)

    label_athletic = Label(page_1, text='Atletismo', bg='#3290F1').place(anchor=NE, x=700, y=70)
    entry_athletic = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=70)

    label_ride = Label(page_1, text='Montar', bg='#3290F1').place(anchor=NE, x=700, y=100)
    entry_ride = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=100)

    label_climb = Label(page_1, text='Trepar', bg='#3290F1').place(anchor=NE, x=700, y=130)
    entry_climb = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=130)

    label_jump = Label(page_1, text='Saltar', bg='#3290F1').place(anchor=NE, x=700, y=160)
    entry_jump = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=160)

    label_drive = Label(page_1, text='Conducir', bg='#3290F1').place(anchor=NE, x=700, y=190)
    entry_drive = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=190)

    separator = Separator(page_1).place(x=630, y=230, width=120, height=2)

    # Social
    label_style = Label(page_1, text='Estilo', bg='#3290F1').place(anchor=NE, x=700, y=250)
    entry_style = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=250)

    label_intimidate = Label(page_1, text='Intimidar', bg='#3290F1').place(anchor=NE, x=700, y=280)
    entry_intimidate = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=280)

    label_leadership = Label(page_1, text='Liderazgo', bg='#3290F1').place(anchor=NE, x=700, y=310)
    entry_leadership = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=310)

    label_persuasion = Label(page_1, text='Persuasión', bg='#3290F1').place(anchor=NE, x=700, y=340)
    entry_persuasion = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=340)

    label_trade = Label(page_1, text='Comercio', bg='#3290F1').place(anchor=NE, x=700, y=370)
    entry_trade = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=370)

    label_wander = Label(page_1, text='Callejear', bg='#3290F1').place(anchor=NE, x=700, y=400)
    entry_wander = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=400)

    label_etiquette = Label(page_1, text='Etiqueta', bg='#3290F1').place(anchor=NE, x=700, y=430)
    entry_etiquette = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=430)

    separator = Separator(page_1).place(x=630, y=470, width=120, height=2)

    # Knowledge
    label_animal = Label(page_1, text='Animales', bg='#3290F1').place(anchor=NE, x=700, y=490)
    entry_animal = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=490)

    label_science = Label(page_1, text='Etiqueta', bg='#3290F1').place(anchor=NE, x=700, y=520)
    entry_science = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=520)

    label_law = Label(page_1, text='Ley', bg='#3290F1').place(anchor=NE, x=700, y=550)
    entry_law = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=550)

    label_plant = Label(page_1, text='Herbolaria', bg='#3290F1').place(anchor=NE, x=700, y=580)
    entry_plant = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=580)

    label_history = Label(page_1, text='Historia', bg='#3290F1').place(anchor=NE, x=700, y=610)
    entry_history = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=610)

    label_tactic = Label(page_1, text='Táctica', bg='#3290F1').place(anchor=NE, x=700, y=640)
    entry_tactic = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=640)

    label_medicine = Label(page_1, text='Medicina', bg='#3290F1').place(anchor=NE, x=700, y=670)
    entry_medicine = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=670)

    label_memorize = Label(page_1, text='Memorizar', bg='#3290F1').place(anchor=NE, x=700, y=700)
    entry_memorize = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=700)

    label_navigation = Label(page_1, text='Navegación', bg='#3290F1').place(anchor=NE, x=700, y=730)
    entry_navigation = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=730)

    label_occultism = Label(page_1, text='Ocultismo', bg='#3290F1').place(anchor=NE, x=700, y=760)
    entry_occultism = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=760)

    label_value = Label(page_1, text='Tasación', bg='#3290F1').place(anchor=NE, x=700, y=790)
    entry_value = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=790)

    label_magic = Label(page_1, text='V.Mágica', bg='#3290F1').place(anchor=NE, x=700, y=820)
    entry_magic = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=820)

    separator = Separator(page_1).place(x=630, y=860, width=120, height=2)

    label_coldness = Label(page_1, text='Frialdad', bg='#3290F1').place(anchor=NE, x=700, y=880)
    entry_coldness = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=880)

    label_strenght = Label(page_1, text='P.Fuerza', bg='#3290F1').place(anchor=NE, x=700, y=910)
    entry_strenght = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=910)

    label_pain = Label(page_1, text='Res.Dolor', bg='#3290F1').place(anchor=NE, x=700, y=940)
    entry_pain = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=940)