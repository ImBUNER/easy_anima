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
    btn1 = Button(topCard, text="Página 2", command=change_page_2, cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn1.place(x=410, y=960)

    btn2 = Button(topCard, text="Página 1", command=change_page_1, cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn2.place(x=300, y=960)

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
        panel.place(x=30, y=40)

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

    label_class = Label(page_2, text='Categoría', bg='#3290F1').place(x=560, y=62)
    entry_class = Entry(page_2, width=25, bg="#f2f2f2").place(x=550, y=80)

    #Row 2
    label_area = Label(page_2, text='Región', bg='#3290F1').place(x=320, y=112)
    entry_area = Entry(page_2, width=25, bg="#f2f2f2").place(x=310, y=130)

    label_social_class = Label(page_2, text='Clase social', bg='#3290F1').place(x=560, y=112)
    entry_social_class = Entry(page_2, width=25, bg="#f2f2f2").place(x=550, y=130)

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

    label_current_experience = Label(page_2, text='Actual', bg='#3290F1').place(x=440, y=262)
    entry_current_experience = Entry(page_2, width=10, bg="#f2f2f2").place(x=430, y=280)

    label_next_level_experience = Label(page_2, text='Sig.Nivel', bg='#3290F1').place(x=560, y=262)
    entry_next_level_experience = Entry(page_2, width=10, bg="#f2f2f2").place(x=550, y=280)

    label_level = Label(page_2, text='Nivel', bg='#3290F1').place(x=680, y=262)
    entry_level = Entry(page_2, width=10, bg="#f2f2f2").place(x=670, y=280)
    
    
    #Character personality ----------------
    label_personality =Label(page_2, text='Personalidad', bg='#3290F1').place(x=40, y=308)
    box_personality = Text(page_2, bg="#f2f2f2", height=5, width=90).place(x=30, y=330)

    #Character history --------------------
    label_history =Label(page_2, text='Historia', bg='#3290F1').place(x=40, y=438)
    box_history = Text(page_2, bg="#f2f2f2", height=10, width=90).place(x=30, y=460)

    #Character combat equipment -----------
    label_combat_equipment =Label(page_2, text='Equipo de combate', bg='#3290F1').place(x=40, y=658)
    box_combat_equipment = Text(page_2, bg="#f2f2f2", height=15, width=42).place(x=30, y=680)

    #Character varied equipment ----------
    label_varied_equipment =Label(page_2, text='Equipo variado', bg='#3290F1').place(x=420, y=658)
    box_varied_equipment = Text(page_2, bg="#f2f2f2", height=15, width=42).place(x=410, y=680)



    





    # PAGE 1 - Character characteristic -----------------------------------------------------------

    # Character stats ---------------------------
    label_stats = Label(page_1, text='Características', bg='#3290F1', font='bold').place(x=150, y=8)
    zone_stats = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="80", width="390").place(x=20, y=30)

    # Row 1
    label_AGI = Label(page_1, text='AGI', bg='#3290F1').place(anchor=NE, x=60, y=42)
    entry_AGI = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=62, y=40)

    label_CON = Label(page_1, text='CON', bg='#3290F1').place(anchor=NE, x=155, y=42)
    entry_CON = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=157, y=40)

    label_DES = Label(page_1, text='DES', bg='#3290F1').place(anchor=NE, x=250, y=42)
    entry_DES = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=252, y=40)

    label_FUE = Label(page_1, text='FUE', bg='#3290F1').place(anchor=NE, x=345, y=42)
    entry_FUE = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=347, y=40)

    # # Row 2
    label_INT = Label(page_1, text='INT', bg='#3290F1').place(anchor=NE, x=60, y=77)
    entry_INT = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=62, y=75)

    label_PER = Label(page_1, text='PER', bg='#3290F1').place(anchor=NE, x=155, y=77)
    entry_PER = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=157, y=75)

    label_POD = Label(page_1, text='POD', bg='#3290F1').place(anchor=NE, x=250, y=77)
    entry_POD = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=252, y=75)

    label_VOL = Label(page_1, text='VOL', bg='#3290F1').place(anchor=NE, x=345, y=77)
    entry_VOL = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER).place(x=347, y=75)


    # Secondary abilities --------------------------
    label_secondary_abilities = Label(page_1, text='Habilidades Secundarias', bg='#3290F1', font='bold').place(x=515, y=8)

    # Column 1
    zone_secondary_abilities_1 = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="950", width="170").place(x=610, y=30)

    # Athletics
    label_acrobatics = Label(page_1, text='Acrobacias', bg='#3290F1').place(anchor=NE, x=700, y=40)
    entry_acrobatics = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=40)

    label_athleticism = Label(page_1, text='Atletismo', bg='#3290F1').place(anchor=NE, x=700, y=70)
    entry_athleticism = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=70)

    label_ride = Label(page_1, text='Montar', bg='#3290F1').place(anchor=NE, x=700, y=100)
    entry_ride = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=100)

    label_climb = Label(page_1, text='Trepar', bg='#3290F1').place(anchor=NE, x=700, y=130)
    entry_climb = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=130)

    label_jump = Label(page_1, text='Saltar', bg='#3290F1').place(anchor=NE, x=700, y=160)
    entry_jump = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=160)

    label_swim = Label(page_1, text='Nadar', bg='#3290F1').place(anchor=NE, x=700, y=190)
    entry_swim = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=190)

    separator_1 = Separator(page_1).place(x=630, y=230, width=130, height=2)

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

    separator_2 = Separator(page_1).place(x=630, y=470, width=130, height=2)

    # Perception
    label_notice = Label(page_1, text='Advertir', bg='#3290F1').place(anchor=NE, x=700, y=490)
    entry_notice = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=490)

    label_search = Label(page_1, text='Buscar', bg='#3290F1').place(anchor=NE, x=700, y=520)
    entry_search = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=520)

    label_track = Label(page_1, text='Rastrear', bg='#3290F1').place(anchor=NE, x=700, y=550)
    entry_track = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=550)

    separator_3 = Separator(page_1).place(x=630, y=590, width=130, height=2)

    # Intellectual
    label_animals = Label(page_1, text='Animales', bg='#3290F1').place(anchor=NE, x=700, y=610)
    entry_animals = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=610)

    label_science = Label(page_1, text='Ciencia', bg='#3290F1').place(anchor=NE, x=700, y=640)
    entry_science = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=640)

    label_law = Label(page_1, text='Ley', bg='#3290F1').place(anchor=NE, x=700, y=670)
    entry_law = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=670)

    label_herballore = Label(page_1, text='Herbolaria', bg='#3290F1').place(anchor=NE, x=700, y=700)
    entry_herballore = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=700)

    label_history = Label(page_1, text='Historia', bg='#3290F1').place(anchor=NE, x=700, y=730)
    entry_history = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=730)

    label_tactic = Label(page_1, text='Táctica', bg='#3290F1').place(anchor=NE, x=700, y=760)
    entry_tactic = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=760)

    label_medicine = Label(page_1, text='Medicina', bg='#3290F1').place(anchor=NE, x=700, y=790)
    entry_medicine = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=790)

    label_memorize = Label(page_1, text='Memorizar', bg='#3290F1').place(anchor=NE, x=700, y=820)
    entry_memorize = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=820)

    label_navigation = Label(page_1, text='Navegación', bg='#3290F1').place(anchor=NE, x=700, y=850)
    entry_navigation = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=850)

    label_occult = Label(page_1, text='Ocultismo', bg='#3290F1').place(anchor=NE, x=700, y=880)
    entry_occult = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=880)

    label_appraisal = Label(page_1, text='Tasación', bg='#3290F1').place(anchor=NE, x=700, y=910)
    entry_appraisal = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=910)

    label_magic_appraisal = Label(page_1, text='V.Mágica', bg='#3290F1').place(anchor=NE, x=700, y=940)
    entry_magic_appraisal = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=710, y=940)

    # Column 2
    zone_secondary_abilities_2 = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="740", width="170").place(x=435, y=30)

    # Vigor
    label_composure = Label(page_1, text='Frialdad', bg='#3290F1').place(anchor=NE, x=525, y=40)
    entry_composure = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=40)

    label_feats_of_strenght = Label(page_1, text='P.Fuerza', bg='#3290F1').place(anchor=NE, x=525, y=70)
    entry_feats_of_strenght = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=70)

    label_withstand_pain = Label(page_1, text='Res.Dolor', bg='#3290F1').place(anchor=NE, x=525, y=100)
    entry_withstand_pain = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=100)

    separator_4 = Separator(page_1).place(x=455, y=140, width=130, height=2)

    # Subterfuge
    label_lock_picking = Label(page_1, text='Cerrajería', bg='#3290F1').place(anchor=NE, x=525, y=160)
    entry_lock_picking = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=160)

    label_disguise = Label(page_1, text='Disfraz', bg='#3290F1').place(anchor=NE, x=525, y=190)
    entry_disguise = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=190)

    label_hide = Label(page_1, text='Ocultarse', bg='#3290F1').place(anchor=NE, x=525, y=220)
    entry_hide = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=220)

    label_theft = Label(page_1, text='Robo', bg='#3290F1').place(anchor=NE, x=525, y=250)
    entry_theft = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=250)

    label_stealth = Label(page_1, text='Sigilo', bg='#3290F1').place(anchor=NE, x=525, y=280)
    entry_stealth = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=280)

    label_trap_lore = Label(page_1, text='Trampería', bg='#3290F1').place(anchor=NE, x=525, y=310)
    entry_trap_lore = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=310)

    label_poisons = Label(page_1, text='Venenos', bg='#3290F1').place(anchor=NE, x=525, y=340)
    entry_poisons = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=340)

    separator_5 = Separator(page_1).place(x=455, y=380, width=130, height=2)

    # Creative
    label_art = Label(page_1, text='Arte', bg='#3290F1').place(anchor=NE, x=525, y=400)
    entry_art = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=400)

    label_dance = Label(page_1, text='Baile', bg='#3290F1').place(anchor=NE, x=525, y=430)
    entry_dance = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=430)

    label_forging = Label(page_1, text='Forja', bg='#3290F1').place(anchor=NE, x=525, y=460)
    entry_forging = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=460)

    label_runes = Label(page_1, text='Runas', bg='#3290F1').place(anchor=NE, x=525, y=490)
    entry_runes = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=490)

    label_alchemy = Label(page_1, text='Alquimia', bg='#3290F1').place(anchor=NE, x=525, y=520)
    entry_alchemy = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=520)

    label_animism = Label(page_1, text='Animismo', bg='#3290F1').place(anchor=NE, x=525, y=550)
    entry_animism = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=550)

    label_music = Label(page_1, text='Música', bg='#3290F1').place(anchor=NE, x=525, y=580)
    entry_music = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=580)

    label_sleight_of_hand = Label(page_1, text='T.Manos', bg='#3290F1').place(anchor=NE, x=525, y=610)
    entry_sleight_of_hand = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=610)

    label_ritual = Label(page_1, text='Cal.Ritual', bg='#3290F1').place(anchor=NE, x=525, y=640)
    entry_ritual = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=640)

    label_goldsmith = Label(page_1, text='Orfebrería', bg='#3290F1').place(anchor=NE, x=525, y=670)
    entry_goldsmith = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=670)

    label_making = Label(page_1, text='Confección', bg='#3290F1').place(anchor=NE, x=525, y=700)
    entry_making = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=700)

    label_puppets = Label(page_1, text='Marionetas', bg='#3290F1').place(anchor=NE, x=525, y=730)
    entry_puppets = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=535, y=730)


    # Life points ---------------------------
    label_life_points = Label(page_1, text='Puntos de vida', bg='#3290F1', font='bold').place(x=155, y=118)
    zone_life_points = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="75", width="390").place(x=20, y=140)

    # Total
    label_life_points_total = Label(page_1, text='Total', bg='#3290F1').place(anchor=NE, x=137, y=145)
    entry_life_points_total = Entry(page_1, width=8, bg="#f2f2f2", justify=CENTER, font=('bold', 22)).place(x=40, y=165)

    # Current
    label_life_points_current = Label(page_1, text='Actual', bg='#3290F1').place(anchor=NE, x=330, y=145)
    entry_life_points_current = Entry(page_1, width=8, bg="#f2f2f2", justify=CENTER, font=('bold', 22)).place(x=230, y=165)


    # Fatigue points ---------------------------
    label_fatigue_points = Label(page_1, text='Cansancio', bg='#3290F1', font='bold').place(x=170, y=228)
    zone_fatigue_points = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="65", width="390").place(x=20, y=250)

    # Total
    label_fatigue_points_total = Label(page_1, text='Total', bg='#3290F1').place(anchor=NE, x=142, y=255)
    entry_fatigue_points_total = Entry(page_1, width=8, bg="#f2f2f2", justify=CENTER, font=('bold', 15)).place(x=70, y=275)

    # Current
    label_fatigue_points_current = Label(page_1, text='Actual', bg='#3290F1').place(anchor=NE, x=328, y=255)
    entry_fatigue_points_current = Entry(page_1, width=8, bg="#f2f2f2", justify=CENTER, font=('bold', 15)).place(x=250, y=275)


    # Primary abilities ----------------------------
    label_primary_abilities = Label(page_1, text='Habilidades de combate', bg='#3290F1', font='bold').place(x=120, y=330)
    zone_primary_abilities = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="170", width="390").place(x=20, y=350)

    # Row 0 - Titles
    label_primary_abilities_base = Label(page_1, text='Base', bg='#3290F1').place(x=152, y=360)
    label_primary_abilities_bonus = Label(page_1, text='Bono', bg='#3290F1').place(x=240, y=360)
    label_primary_abilities_penalizer = Label(page_1, text='Penaliz.', bg='#3290F1').place(x=325, y=360)

    # Row 1 - Attack
    label_attack = Label(page_1, text='H.Ataque', bg='#3290F1', font='bold').place(anchor=NE, x=120, y=383)
    entry_attack_base = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15)).place(x=135, y=380)
    entry_attack_bonus = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15)).place(x=225, y=380)
    entry_attack_penalizer = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15)).place(x=315, y=380)

    # Row 2 - Defense
    label_defense = Label(page_1, text='H.Defensa', bg='#3290F1', font='bold').place(anchor=NE, x=120, y=423)
    entry_defense_base = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15)).place(x=135, y=420)
    entry_defense_bonus = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15)).place(x=225, y=420)
    entry_defense_penalizer = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15)).place(x=315, y=420)

    # Row 3 - Others
    # Initiative
    label_initiative = Label(page_1, text='Turno', bg='#3290F1', font='bold').place(anchor=NE, x=105, y=460)
    entry_initiative = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15)).place(x=45, y=480)

    # Armor
    label_armor = Label(page_1, text='TA', bg='#3290F1', font='bold').place(anchor=NE, x=182, y=460)
    entry_armor = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15)).place(x=135, y=480)

    # Weapon damage
    label_damage = Label(page_1, text='Daño', bg='#3290F1', font='bold').place(anchor=NE, x=285, y=460)
    entry_damage = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15)).place(x=225, y=480)

    # Weapon quality
    label_quality = Label(page_1, text='Calidad', bg='#3290F1', font='bold').place(anchor=NE, x=380, y=460)
    entry_quality = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15)).place(x=315, y=480)


    # Creation points -----------------------
    label_creation_points = Label(page_1, text='Puntos de creación', bg='#3290F1', font='bold').place(x=135, y=535)
    zone_creation_points = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="215", width="390").place(x=20, y=555)
    
    # Advantages
    label_advantages = Label(page_1, text='Ventajas', bg='#3290F1').place(x=50, y=565)
    box_advantages = Text(page_1, bg="#f2f2f2", height=4, width=45).place(x=31, y=585)

    # Disadvantages
    label_advantages = Label(page_1, text='Desventajas', bg='#3290F1').place(x=48, y=665)
    box_disadvantages = Text(page_1, bg="#f2f2f2", height=4, width=45).place(x=31, y=685)
    

    # Resistances ---------------------------
    label_resistance = Label(page_1, text='Resistencias', bg='#3290F1', font='bold').place(x=165, y=785)
    zone_resistance = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="60", width="575").place(x=15, y=805)

    label_base_presence = Label(page_1, text='Pres.Base', bg='#3290F1').place(x=55, y=812)
    entry_base_presence = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=60, y=832)

    label_physical_resistance = Label(page_1, text='RF', bg='#3290F1').place(x=187, y=812)
    entry_physical_resistance = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=170, y=832)

    label_disease_resistance = Label(page_1, text='RE', bg='#3290F1').place(x=267, y=812)
    entry_disease_resistance = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=250, y=832)

    label_venom_resistance = Label(page_1, text='RV', bg='#3290F1').place(x=347, y=812)
    entry_venom_resistance = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=330, y=832)

    label_magic_resistance = Label(page_1, text='RM', bg='#3290F1').place(x=427, y=812)
    entry_magic_resistance = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=410, y=832)

    label_psychic_resistance = Label(page_1, text='RP', bg='#3290F1').place(x=507, y=812)
    entry_psychic_resistance = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER).place(x=490, y=832)


    # Buttoms -------------------------------
    zone_buttoms = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="60", width="575").place(x=15, y=880)

    btn_initiative = Button(topCard, text="Turno", cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn_initiative.place(x=32, y=895)

    btn_combat = Button(topCard, text="Combate", cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn_combat.place(x=113, y=895)

    # btn_defense = Button(topCard, text="Defender", cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    # btn_defense.place(x=185, y=895)

    btn_secondary = Button(topCard, text="Secundaria", cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn_secondary.place(x=217, y=895)

    btn_stat = Button(topCard, text="Característica", cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn_stat.place(x=335, y=895)

    btn_resistance = Button(topCard, text="Resistencia", cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD')
    btn_resistance.place(x=470, y=895)