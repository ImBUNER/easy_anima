from tkinter import CENTER, NE, RIDGE, OptionMenu, StringVar, Toplevel, Frame, Label, Button, Entry, Text, END
from tkinter.ttk import Separator
from PIL import Image, ImageTk
from tkinter import filedialog
import card_manager
import history_manager

# Variables globales para llamar en otros modulos
page_1 = None
page_2 = None
topCard = None
combat = None
resistence = None
secondary = None
caracteristic = None

def open(es_nueva_ficha):
    global page_2, page_1, topCard, resistence, combat, secondary, caracteristic
    topCard = Toplevel()
    topCard.title('página en blanco - Easy Anima')
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


    # Page change buttons ------
    btn1 = Button(topCard, text="Página 1", command=change_page_1, cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', width=5)
    btn1.place(x=30, y=960)

    btn2 = Button(topCard, text="Página 2", command=change_page_2, cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', width=5)
    btn2.place(x=110, y=960)

    # Info about the current page
    info_page_1 = Label(page_1, text='Atributos - pagina 1', bg='#3290F1')
    info_page_1.place(x=190, y=970)
    
    info_page_2 = Label(page_2, text='Transfondo - pagina 2', bg='#3290F1')
    info_page_2.place(x=190, y=970)

    # Default page
    change_page_1()

    # Save file button ------
    btn_save = Button(topCard, text="Guardar", cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', width=5, 
                        command=lambda : card_manager.guardar_personaje(card_manager.lista_entrys_y_labels))
    btn_save.place(x=440, y=960)

    # Delete file button ----
    btn_delete = Button(topCard, text="Eliminar", cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', width=5,
                        command=lambda : card_manager.eliminar_personaje(referencia_ventana_pj = topCard))
    btn_delete.place(x=520, y=960)

    

    # Character image
    def image():
        # Choose and open the image
        x = open_image()

        img = Image.open(x)

        # if not img.endswith('.png'):
        #     print('error')
        #     return

        # Resize and filter the image
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
    
        # Image label
        panel_image = Label(page_2, image=None)
        panel_image.place(x=30, y=40)
        panel_image.image = img

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
    label_name = Label(page_2, text='Nombre / Apodo', bg='#3290F1')
    label_name.place(x=320, y=12)
    entry_name = Entry(page_2, width=55, bg="#f2f2f2", name="nombre_pj" )
    entry_name.place(x=310, y=30)

    #Row 1
    label_race = Label(page_2, text='Raza', bg='#3290F1')
    label_race.place(x=320, y=62)
    entry_race = Entry(page_2, width=25, bg="#f2f2f2")
    entry_race.place(x=310, y=80)

    label_class = Label(page_2, text='Categoría', bg='#3290F1')
    label_class.place(x=560, y=62)
    entry_class = Entry(page_2, width=25, bg="#f2f2f2")
    entry_class.place(x=550, y=80)

    #Row 2
    label_area = Label(page_2, text='Región', bg='#3290F1')
    label_area.place(x=320, y=112)
    entry_area = Entry(page_2, width=25, bg="#f2f2f2")
    entry_area.place(x=310, y=130)

    label_social_class = Label(page_2, text='Clase social', bg='#3290F1')
    label_social_class.place(x=560, y=112)
    entry_social_class = Entry(page_2, width=25, bg="#f2f2f2")
    entry_social_class.place(x=550, y=130)

    #Row 3
    label_height = Label(page_2, text='Altura (m)', bg='#3290F1')
    label_height.place(x=320, y=162)
    entry_height = Entry(page_2, width=10, bg="#f2f2f2")
    entry_height.place(x=310, y=180)

    label_weight = Label(page_2, text='Peso (kg)', bg='#3290F1')
    label_weight.place(x=440, y=162)
    entry_weight = Entry(page_2, width=10, bg="#f2f2f2")
    entry_weight.place(x=430, y=180)

    label_eyes = Label(page_2, text='Ojos', bg='#3290F1')
    label_eyes.place(x=560, y=162)
    entry_eyes = Entry(page_2, width=10, bg="#f2f2f2")
    entry_eyes.place(x=550, y=180)

    label_hair = Label(page_2, text='Cabello', bg='#3290F1')
    label_hair.place(x=680, y=162)
    entry_hair = Entry(page_2, width=10, bg="#f2f2f2")
    entry_hair.place(x=670, y=180)

    #Row 4
    label_gender = Label(page_2, text='Género', bg='#3290F1')
    label_gender.place(x=320, y=212)
    entry_gender = Entry(page_2, width=10, bg="#f2f2f2")
    entry_gender.place(x=310, y=230)

    label_age = Label(page_2, text='Edad', bg='#3290F1')
    label_age.place(x=440, y=212)
    entry_age = Entry(page_2, width=10, bg="#f2f2f2")
    entry_age.place(x=430, y=230)

    label_skin = Label(page_2, text='Tez', bg='#3290F1')
    label_skin.place(x=560, y=212)
    entry_skin = Entry(page_2, width=10, bg="#f2f2f2")
    entry_skin.place(x=550, y=230)

    label_ethnic = Label(page_2, text='Etnia', bg='#3290F1')
    label_ethnic.place(x=680, y=212)
    entry_ethnic = Entry(page_2, width=10, bg="#f2f2f2")
    entry_ethnic.place(x=670, y=230)

    #Row 5
    label_experiencie = Label(page_2, text='Experiencia:', bg='#3290F1').place(x=320, y=282)

    label_current_experience = Label(page_2, text='Ex-Actual', bg='#3290F1')
    label_current_experience.place(x=440, y=262)
    entry_current_experience = Entry(page_2, width=10, bg="#f2f2f2")
    entry_current_experience.place(x=430, y=280)

    label_next_level_experience = Label(page_2, text='Sig.Nivel', bg='#3290F1')
    label_next_level_experience.place(x=560, y=262)
    entry_next_level_experience = Entry(page_2, width=10, bg="#f2f2f2")
    entry_next_level_experience.place(x=550, y=280)

    label_level = Label(page_2, text='Nivel', bg='#3290F1')
    label_level.place(x=680, y=262)
    entry_level = Entry(page_2, width=10, bg="#f2f2f2")
    entry_level.place(x=670, y=280)
    
    
    #Character personality ----------------
    label_personality =Label(page_2, text='Personalidad', bg='#3290F1')
    label_personality.place(x=40, y=308)
    box_personality = Text(page_2, bg="#f2f2f2", height=5, width=90)
    box_personality.place(x=30, y=330)

    #Character history --------------------
    label_char_history = Label(page_2, text='Pj-Historia', bg='#3290F1')
    label_char_history.place(x=40, y=438)
    box_char_history = Text(page_2, bg="#f2f2f2", height=10, width=90)
    box_char_history.place(x=30, y=460)

    #Character combat equipment -----------
    label_combat_equipment = Label(page_2, text='Equipo de combate', bg='#3290F1')
    label_combat_equipment.place(x=40, y=658)
    box_combat_equipment = Text(page_2, bg="#f2f2f2", height=15, width=42)
    box_combat_equipment.place(x=30, y=680)

    #Character varied equipment ----------
    label_varied_equipment =Label(page_2, text='Equipo variado', bg='#3290F1')
    label_varied_equipment.place(x=420, y=658)
    box_varied_equipment = Text(page_2, bg="#f2f2f2", height=15, width=42)
    box_varied_equipment.place(x=410, y=680)



    





    # PAGE 1 - Character characteristic -----------------------------------------------------------

    # Character stats ---------------------------
    label_stats = Label(page_1, text='Características', bg='#3290F1', font='bold').place(x=150, y=8)
    zone_stats = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="80", width="390").place(x=20, y=30)

    # Row 1
    label_AGI = Label(page_1, text='AGI', bg='#3290F1')
    label_AGI.place(anchor=NE, x=60, y=42)
    entry_AGI = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, name="agi")
    entry_AGI.place(x=62, y=40)

    label_CON = Label(page_1, text='CON', bg='#3290F1')
    label_CON.place(anchor=NE, x=155, y=42)
    entry_CON = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, name="con")
    entry_CON.place(x=157, y=40)

    label_DES = Label(page_1, text='DES', bg='#3290F1')
    label_DES.place(anchor=NE, x=250, y=42)
    entry_DES = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, name="des")
    entry_DES.place(x=252, y=40)

    label_FUE = Label(page_1, text='FUE', bg='#3290F1')
    label_FUE.place(anchor=NE, x=345, y=42)
    entry_FUE = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, name="fue")
    entry_FUE.place(x=347, y=40)

    # # Row 2
    label_INT = Label(page_1, text='INT', bg='#3290F1')
    label_INT.place(anchor=NE, x=60, y=77)
    entry_INT = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, name="int")
    entry_INT.place(x=62, y=75)

    label_PER = Label(page_1, text='PER', bg='#3290F1')
    label_PER.place(anchor=NE, x=155, y=77)
    entry_PER = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, name="per")
    entry_PER.place(x=157, y=75)

    label_POD = Label(page_1, text='POD', bg='#3290F1')
    label_POD.place(anchor=NE, x=250, y=77)
    entry_POD = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, name="pod")
    entry_POD.place(x=252, y=75)

    label_VOL = Label(page_1, text='VOL', bg='#3290F1')
    label_VOL.place(anchor=NE, x=345, y=77)
    entry_VOL = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, name="vol")
    entry_VOL.place(x=347, y=75)


    # Secondary abilities --------------------------
    label_secondary_abilities = Label(page_1, text='Habilidades Secundarias', bg='#3290F1', font='bold').place(x=515, y=8)

    # Column 1
    zone_secondary_abilities_1 = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="950", width="170").place(x=610, y=30)

    # Athletics
    label_acrobatics = Label(page_1, text='Acrobacias', bg='#3290F1')
    label_acrobatics.place(anchor=NE, x=700, y=40)
    entry_acrobatics = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="acrobacias")
    entry_acrobatics.place(x=710, y=40)

    label_athleticism = Label(page_1, text='Atletismo', bg='#3290F1')
    label_athleticism.place(anchor=NE, x=700, y=70)
    entry_athleticism = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="atletismo")
    entry_athleticism.place(x=710, y=70)

    label_ride = Label(page_1, text='Montar', bg='#3290F1')
    label_ride.place(anchor=NE, x=700, y=100)
    entry_ride = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="montar")
    entry_ride.place(x=710, y=100)

    label_climb = Label(page_1, text='Trepar', bg='#3290F1')
    label_climb.place(anchor=NE, x=700, y=130)
    entry_climb = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="trepar")
    entry_climb.place(x=710, y=130)

    label_jump = Label(page_1, text='Saltar', bg='#3290F1')
    label_jump.place(anchor=NE, x=700, y=160)
    entry_jump = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="saltar")
    entry_jump.place(x=710, y=160)

    label_swim = Label(page_1, text='Nadar', bg='#3290F1')
    label_swim.place(anchor=NE, x=700, y=190)
    entry_swim = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="nadar")
    entry_swim.place(x=710, y=190)

    separator_1 = Separator(page_1).place(x=630, y=230, width=130, height=2)

    # Social
    label_style = Label(page_1, text='Estilo', bg='#3290F1')
    label_style.place(anchor=NE, x=700, y=250)
    entry_style = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="estilo")
    entry_style.place(x=710, y=250)

    label_intimidate = Label(page_1, text='Intimidar', bg='#3290F1')
    label_intimidate.place(anchor=NE, x=700, y=280)
    entry_intimidate = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="intimidar")
    entry_intimidate.place(x=710, y=280)

    label_leadership = Label(page_1, text='Liderazgo', bg='#3290F1')
    label_leadership.place(anchor=NE, x=700, y=310)
    entry_leadership = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="liderazgo")
    entry_leadership.place(x=710, y=310)

    label_persuasion = Label(page_1, text='Persuasión', bg='#3290F1')
    label_persuasion.place(anchor=NE, x=700, y=340)
    entry_persuasion = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="persuacion")
    entry_persuasion.place(x=710, y=340)

    label_trade = Label(page_1, text='Comercio', bg='#3290F1')
    label_trade.place(anchor=NE, x=700, y=370)
    entry_trade = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="comercio")
    entry_trade.place(x=710, y=370)

    label_wander = Label(page_1, text='Callejear', bg='#3290F1')
    label_wander.place(anchor=NE, x=700, y=400)
    entry_wander = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="callejear")
    entry_wander.place(x=710, y=400)

    label_etiquette = Label(page_1, text='Etiqueta', bg='#3290F1')
    label_etiquette.place(anchor=NE, x=700, y=430)
    entry_etiquette = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="etiqueta")
    entry_etiquette.place(x=710, y=430)

    separator_2 = Separator(page_1).place(x=630, y=470, width=130, height=2)

    # Perception
    label_notice = Label(page_1, text='Advertir', bg='#3290F1')
    label_notice.place(anchor=NE, x=700, y=490)
    entry_notice = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="advertir")
    entry_notice.place(x=710, y=490)

    label_search = Label(page_1, text='Buscar', bg='#3290F1')
    label_search.place(anchor=NE, x=700, y=520)
    entry_search = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="buscar")
    entry_search.place(x=710, y=520)

    label_track = Label(page_1, text='Rastrear', bg='#3290F1')
    label_track.place(anchor=NE, x=700, y=550)
    entry_track = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="rastrear")
    entry_track.place(x=710, y=550)

    separator_3 = Separator(page_1).place(x=630, y=590, width=130, height=2)

    # Intellectual
    label_animals = Label(page_1, text='Animales', bg='#3290F1')
    label_animals.place(anchor=NE, x=700, y=610)
    entry_animals = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="animales")
    entry_animals.place(x=710, y=610)

    label_science = Label(page_1, text='Ciencia', bg='#3290F1')
    label_science.place(anchor=NE, x=700, y=640)
    entry_science = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="ciencia")
    entry_science.place(x=710, y=640)

    label_law = Label(page_1, text='Ley', bg='#3290F1')
    label_law.place(anchor=NE, x=700, y=670)
    entry_law = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="ley")
    entry_law.place(x=710, y=670)

    label_herballore = Label(page_1, text='Herbolaria', bg='#3290F1')
    label_herballore.place(anchor=NE, x=700, y=700)
    entry_herballore = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="herbolaria")
    entry_herballore.place(x=710, y=700)

    label_history = Label(page_1, text='Historia', bg='#3290F1')
    label_history.place(anchor=NE, x=700, y=730)
    entry_history = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="historia")
    entry_history.place(x=710, y=730)

    label_tactic = Label(page_1, text='Táctica', bg='#3290F1')
    label_tactic.place(anchor=NE, x=700, y=760)
    entry_tactic = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="tactica")
    entry_tactic.place(x=710, y=760)

    label_medicine = Label(page_1, text='Medicina', bg='#3290F1')
    label_medicine.place(anchor=NE, x=700, y=790)
    entry_medicine = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="medicina")
    entry_medicine.place(x=710, y=790)

    label_memorize = Label(page_1, text='Memorizar', bg='#3290F1')
    label_memorize.place(anchor=NE, x=700, y=820)
    entry_memorize = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="memorizar")
    entry_memorize.place(x=710, y=820)

    label_navigation = Label(page_1, text='Navegación', bg='#3290F1')
    label_navigation.place(anchor=NE, x=700, y=850)
    entry_navigation = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="navegacion")
    entry_navigation.place(x=710, y=850)

    label_occult = Label(page_1, text='Ocultismo', bg='#3290F1')
    label_occult.place(anchor=NE, x=700, y=880)
    entry_occult = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="ocultismo")
    entry_occult.place(x=710, y=880)

    label_appraisal = Label(page_1, text='Tasación', bg='#3290F1')
    label_appraisal.place(anchor=NE, x=700, y=910)
    entry_appraisal = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="tasacion")
    entry_appraisal.place(x=710, y=910)

    label_magic_appraisal = Label(page_1, text='V.Mágica', bg='#3290F1')
    label_magic_appraisal.place(anchor=NE, x=700, y=940)
    entry_magic_appraisal = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="v_magica")
    entry_magic_appraisal.place(x=710, y=940)

    # Column 2
    zone_secondary_abilities_2 = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="740", width="170").place(x=435, y=30)

    # Vigor
    label_composure = Label(page_1, text='Frialdad', bg='#3290F1')
    label_composure.place(anchor=NE, x=525, y=40)
    entry_composure = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="frialdad")
    entry_composure.place(x=535, y=40)

    label_feats_of_strenght = Label(page_1, text='P.Fuerza', bg='#3290F1')
    label_feats_of_strenght.place(anchor=NE, x=525, y=70)
    entry_feats_of_strenght = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="p_fuerza")
    entry_feats_of_strenght.place(x=535, y=70)

    label_withstand_pain = Label(page_1, text='Res.Dolor', bg='#3290F1')
    label_withstand_pain.place(anchor=NE, x=525, y=100)
    entry_withstand_pain = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="res_dolor")
    entry_withstand_pain.place(x=535, y=100)

    separator_4 = Separator(page_1).place(x=455, y=140, width=130, height=2)

    # Subterfuge
    label_lock_picking = Label(page_1, text='Cerrajería', bg='#3290F1')
    label_lock_picking.place(anchor=NE, x=525, y=160)
    entry_lock_picking = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="cerrajeria")
    entry_lock_picking.place(x=535, y=160)

    label_disguise = Label(page_1, text='Disfraz', bg='#3290F1')
    label_disguise.place(anchor=NE, x=525, y=190)
    entry_disguise = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="disfraz")
    entry_disguise.place(x=535, y=190)

    label_hide = Label(page_1, text='Ocultarse', bg='#3290F1')
    label_hide.place(anchor=NE, x=525, y=220)
    entry_hide = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="ocultarse")
    entry_hide.place(x=535, y=220)

    label_theft = Label(page_1, text='Robo', bg='#3290F1')
    label_theft.place(anchor=NE, x=525, y=250)
    entry_theft = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="robo")
    entry_theft.place(x=535, y=250)

    label_stealth = Label(page_1, text='Sigilo', bg='#3290F1')
    label_stealth.place(anchor=NE, x=525, y=280)
    entry_stealth = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="sigilo")
    entry_stealth.place(x=535, y=280)

    label_trap_lore = Label(page_1, text='Trampería', bg='#3290F1')
    label_trap_lore.place(anchor=NE, x=525, y=310)
    entry_trap_lore = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="tramperia")
    entry_trap_lore.place(x=535, y=310)

    label_poisons = Label(page_1, text='Venenos', bg='#3290F1')
    label_poisons.place(anchor=NE, x=525, y=340)
    entry_poisons = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="venenos")
    entry_poisons.place(x=535, y=340)

    separator_5 = Separator(page_1).place(x=455, y=380, width=130, height=2)

    # Creative
    label_art = Label(page_1, text='Arte', bg='#3290F1')
    label_art.place(anchor=NE, x=525, y=400)
    entry_art = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="arte")
    entry_art.place(x=535, y=400)

    label_dance = Label(page_1, text='Baile', bg='#3290F1')
    label_dance.place(anchor=NE, x=525, y=430)
    entry_dance = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="baile")
    entry_dance.place(x=535, y=430)

    label_forging = Label(page_1, text='Forja', bg='#3290F1')
    label_forging.place(anchor=NE, x=525, y=460)
    entry_forging = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="forja")
    entry_forging.place(x=535, y=460)

    label_runes = Label(page_1, text='Runas', bg='#3290F1')
    label_runes.place(anchor=NE, x=525, y=490)
    entry_runes = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="runas")
    entry_runes.place(x=535, y=490)

    label_alchemy = Label(page_1, text='Alquimia', bg='#3290F1')
    label_alchemy.place(anchor=NE, x=525, y=520)
    entry_alchemy = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="alquimia")
    entry_alchemy.place(x=535, y=520)

    label_animism = Label(page_1, text='Animismo', bg='#3290F1')
    label_animism.place(anchor=NE, x=525, y=550)
    entry_animism = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="animismo")
    entry_animism.place(x=535, y=550)

    label_music = Label(page_1, text='Música', bg='#3290F1')
    label_music.place(anchor=NE, x=525, y=580)
    entry_music = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="musica")
    entry_music.place(x=535, y=580)

    label_sleight_of_hand = Label(page_1, text='T.Manos', bg='#3290F1')
    label_sleight_of_hand.place(anchor=NE, x=525, y=610)
    entry_sleight_of_hand = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="t_manos")
    entry_sleight_of_hand.place(x=535, y=610)

    label_ritual = Label(page_1, text='Cal.Ritual', bg='#3290F1')
    label_ritual.place(anchor=NE, x=525, y=640)
    entry_ritual = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="cal_ritual")
    entry_ritual.place(x=535, y=640)

    label_goldsmith = Label(page_1, text='Orfebrería', bg='#3290F1')
    label_goldsmith.place(anchor=NE, x=525, y=670)
    entry_goldsmith = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="orfebreria")
    entry_goldsmith.place(x=535, y=670)

    label_making = Label(page_1, text='Confección', bg='#3290F1')
    label_making.place(anchor=NE, x=525, y=700)
    entry_making = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="confeccion")
    entry_making.place(x=535, y=700)

    label_puppets = Label(page_1, text='Marionetas', bg='#3290F1')
    label_puppets.place(anchor=NE, x=525, y=730)
    entry_puppets = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="marionetas")
    entry_puppets.place(x=535, y=730)


    # Life points ---------------------------
    label_life_points = Label(page_1, text='Puntos de vida', bg='#3290F1', font='bold').place(x=155, y=118)
    zone_life_points = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="75", width="390").place(x=20, y=140)

    # Total
    label_life_points_total = Label(page_1, text='PV-Total', bg='#3290F1')
    label_life_points_total.place(anchor=NE, x=137, y=145)
    entry_life_points_total = Entry(page_1, width=8, bg="#f2f2f2", justify=CENTER, font=('bold', 22))
    entry_life_points_total.place(x=40, y=165)

    # Current
    label_life_points_current = Label(page_1, text='PV-Actual', bg='#3290F1')
    label_life_points_current.place(anchor=NE, x=330, y=145)
    entry_life_points_current = Entry(page_1, width=8, bg="#f2f2f2", justify=CENTER, font=('bold', 22))
    entry_life_points_current.place(x=230, y=165)


    # Fatigue points ---------------------------
    label_fatigue_points = Label(page_1, text='Cansancio', bg='#3290F1', font='bold').place(x=170, y=228)
    zone_fatigue_points = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="65", width="390").place(x=20, y=250)

    # Total
    label_fatigue_points_total = Label(page_1, text='Fatigue-Total', bg='#3290F1')
    label_fatigue_points_total.place(anchor=NE, x=142, y=255)
    entry_fatigue_points_total = Entry(page_1, width=8, bg="#f2f2f2", justify=CENTER, font=('bold', 15))
    entry_fatigue_points_total.place(x=70, y=275)

    # Current
    label_fatigue_points_current = Label(page_1, text='Fatigue-Actual', bg='#3290F1')
    label_fatigue_points_current.place(anchor=NE, x=328, y=255)
    entry_fatigue_points_current = Entry(page_1, width=8, bg="#f2f2f2", justify=CENTER, font=('bold', 15))
    entry_fatigue_points_current.place(x=250, y=275)


    # Primary abilities ----------------------------
    label_primary_abilities = Label(page_1, text='Habilidades de combate', bg='#3290F1', font='bold').place(x=120, y=330)
    zone_primary_abilities = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="170", width="390").place(x=20, y=350)

    # Row 0 - Titles
    label_primary_abilities_base = Label(page_1, text='Base', bg='#3290F1').place(x=152, y=360)
    label_primary_abilities_bonus = Label(page_1, text='Bono', bg='#3290F1').place(x=240, y=360)
    label_primary_abilities_penalizer = Label(page_1, text='Penaliz.', bg='#3290F1').place(x=325, y=360)

    # Row 1 - Attack
    label_attack = Label(page_1, text='H.Ataque', bg='#3290F1', font='bold')
    label_attack.place(anchor=NE, x=120, y=383)
    entry_attack_base = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15), name="atk-base")
    entry_attack_base.place(x=135, y=380)
    entry_attack_bonus = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15), name="atk-bonus")
    entry_attack_bonus.place(x=225, y=380)
    entry_attack_penalizer = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15), name="atk-penalizer")
    entry_attack_penalizer.place(x=315, y=380)

    # Row 2 - Defense
    label_defense = Label(page_1, text='H.Defensa', bg='#3290F1', font='bold')
    label_defense.place(anchor=NE, x=120, y=423)
    entry_defense_base = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15), name="def-base")
    entry_defense_base.place(x=135, y=420)
    entry_defense_bonus = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15), name="def-bonus")
    entry_defense_bonus.place(x=225, y=420)
    entry_defense_penalizer = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15), name="def-penalizer")
    entry_defense_penalizer.place(x=315, y=420)

    # Row 3 - Others
    # Initiative
    label_initiative = Label(page_1, text='Turno', bg='#3290F1', font='bold')
    label_initiative.place(anchor=NE, x=105, y=460)
    entry_initiative = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15),
        name='turno')
    entry_initiative.place(x=45, y=480)

    # Armor
    label_armor = Label(page_1, text='TA', bg='#3290F1', font='bold')
    label_armor.place(anchor=NE, x=182, y=460)
    entry_armor = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15))
    entry_armor.place(x=135, y=480)

    # Weapon damage
    label_damage = Label(page_1, text='Daño', bg='#3290F1', font='bold')
    label_damage.place(anchor=NE, x=285, y=460)
    entry_damage = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15))
    entry_damage.place(x=225, y=480)

    # Weapon quality
    label_quality = Label(page_1, text='Calidad', bg='#3290F1', font='bold')
    label_quality.place(anchor=NE, x=380, y=460)
    entry_quality = Entry(page_1, width=5, bg="#f2f2f2", justify=CENTER, font=('bold', 15))
    entry_quality.place(x=315, y=480)


    # Creation points -----------------------
    label_creation_points = Label(page_1, text='Puntos de creación', bg='#3290F1', font='bold')
    label_creation_points.place(x=135, y=535)
    zone_creation_points = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="215", width="390")
    zone_creation_points.place(x=20, y=555)
    
    # Advantages
    label_advantages = Label(page_1, text='Ventajas', bg='#3290F1')
    label_advantages.place(x=50, y=565)
    box_advantages = Text(page_1, bg="#f2f2f2", height=4, width=45)
    box_advantages.place(x=31, y=585)

    # Disadvantages
    label_disadvantages = Label(page_1, text='Desventajas', bg='#3290F1')
    label_disadvantages.place(x=48, y=665)
    box_disadvantages = Text(page_1, bg="#f2f2f2", height=4, width=45)
    box_disadvantages.place(x=31, y=685)
    

    # Resistances ---------------------------
    label_resistance = Label(page_1, text='Resistencias', bg='#3290F1', font='bold').place(x=165, y=785)
    zone_resistance = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="60", width="575").place(x=15, y=805)

    label_base_presence = Label(page_1, text='Pres.Base', bg='#3290F1')
    label_base_presence.place(x=55, y=812)
    entry_base_presence = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="presence")
    entry_base_presence.place(x=60, y=832)

    label_physical_resistance = Label(page_1, text='RF', bg='#3290F1')
    label_physical_resistance.place(x=187, y=812)
    entry_physical_resistance = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="rf")
    entry_physical_resistance.place(x=170, y=832)

    label_disease_resistance = Label(page_1, text='RE', bg='#3290F1')
    label_disease_resistance.place(x=267, y=812)
    entry_disease_resistance = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="re")
    entry_disease_resistance.place(x=250, y=832)

    label_venom_resistance = Label(page_1, text='RV', bg='#3290F1')
    label_venom_resistance.place(x=347, y=812)
    entry_venom_resistance = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER,  name="rv")
    entry_venom_resistance.place(x=330, y=832)

    label_magic_resistance = Label(page_1, text='RM', bg='#3290F1')
    label_magic_resistance.place(x=427, y=812)
    entry_magic_resistance = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="rm")
    entry_magic_resistance.place(x=410, y=832)

    label_psychic_resistance = Label(page_1, text='RP', bg='#3290F1')
    label_psychic_resistance.place(x=507, y=812)
    entry_psychic_resistance = Entry(page_1, width=6, bg="#f2f2f2", justify=CENTER, name="rp")
    entry_psychic_resistance.place(x=490, y=832)


    # Buttoms -------------------------------
    zone_buttoms = Frame(page_1, relief=RIDGE, bg='#3290F1', bd="5", height="60", width="575").place(x=15, y=880)

    # Iniciativa ---
    btn_initiative = Button(page_1, 
        command=lambda :history_manager.alterar_historial(tipo_de_modificacion='turno'),
        text="Turno", 
        cursor="fleur", 
        bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD',
                            )
    btn_initiative.place(x=32, y=895)

    # Combate ---
    btn_combat = Button(page_1, text="Combate", cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD',
        command=lambda :history_manager.alterar_historial(tipo_de_modificacion='combate'))
    btn_combat.place(x=113, y=895)

    combat_arr_dropmenu = ["Ataque", "Defensa"]
    combat = StringVar(topCard)

    combat.set(combat_arr_dropmenu[0])
    drop_combat = OptionMenu(page_1, combat, *combat_arr_dropmenu)
    drop_combat.place(x=113, y=925)

    # Secundarias ---
    btn_secondary = Button(page_1, text="Secundaria", cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD',
        command=lambda :history_manager.alterar_historial(tipo_de_modificacion='secundarias'))
    btn_secondary.place(x=217, y=895)

    secund_arr_dropmenu = [
        "acrobacias", "atletismo", "montar", "trepar", "saltar", "nadar",
        "estilo", "intimidar", "liderazgo", "persuasion", "comercio",
        "callejear", "etiqueta", "advertir", "buscar", "rastrear","animales",
        "ciencia", "ley", "herbolaria", "historia", "tactica", "medicina",
        "memorizar", "navegacion", "ocultismo", "tasacion", "v_magica",
        "frialdad", "p_fuerza", "res_dolor", "cerrajeria","disfraz", "ocultarse",
        "robo", "sigilo", "tramperia", "venenos", "arte", "baile", "forja",
        "runas", "alquimia", "animismo", "musica", "t_manos", "cal_ritual",
        "orfebreria", "confeccion", "marionetas"
    ]
    secondary = StringVar(topCard)

    secondary.set(secund_arr_dropmenu[0])
    drop_secundary = OptionMenu(page_1, secondary, *[name.title() for name in secund_arr_dropmenu])
    drop_secundary.place(x=217, y=925)

    # Caracteristicas ---
    btn_stat = Button(page_1, text="Característica", cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD',
        command=lambda :history_manager.alterar_historial(tipo_de_modificacion='caracteristica'))
    btn_stat.place(x=335, y=895)

    caract_arr_dropmenu = ["agi", "con", "des", "fue","int", "per", "pod", "vol"]
    caracteristic = StringVar(topCard)

    caracteristic.set(caract_arr_dropmenu[0])
    drop_caracteristic = OptionMenu(page_1, caracteristic, *caract_arr_dropmenu)
    drop_caracteristic.place(x=335, y=925)

    # Resistencias ---
    btn_resistance = Button(page_1, text="Resistencia", cursor="fleur", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD',
        command=lambda :history_manager.alterar_historial(tipo_de_modificacion='resistencias'))
    btn_resistance.place(x=470, y=895)

    resis_arr_dropmenu = ["presence", "rf", "re", "rv", "rm", "rp"]
    resistence = StringVar(topCard)

    resistence.set(resis_arr_dropmenu[0])
    drop_resistance = OptionMenu(page_1, resistence, *resis_arr_dropmenu)
    drop_resistance.place(x=470, y=925)

    card_manager.lista_entrys_y_labels = [
            [entry_name, label_name],
            [entry_race, label_race],
            [entry_class, label_class],
            [entry_area, label_area],
            [entry_social_class, label_social_class],
            [entry_height, label_height],
            [entry_weight, label_weight],
            [entry_eyes, label_eyes],
            [entry_hair, label_hair],
            [entry_gender, label_gender],
            [entry_age, label_age],
            [entry_skin, label_skin],
            [entry_ethnic, label_ethnic],
            [entry_current_experience, label_current_experience],
            [entry_next_level_experience, label_next_level_experience],
            [entry_level, label_level],
            [entry_AGI, label_AGI],
            [entry_CON, label_CON],
            [entry_DES, label_DES],
            [entry_FUE, label_FUE],
            [entry_INT, label_INT],
            [entry_PER, label_PER],
            [entry_POD, label_POD],
            [entry_VOL, label_VOL],
            [entry_acrobatics, label_acrobatics],
            [entry_athleticism, label_athleticism],
            [entry_ride, label_ride],
            [entry_climb, label_climb],
            [entry_jump, label_jump],
            [entry_swim, label_swim],
            [entry_style, label_style],
            [entry_intimidate, label_intimidate],
            [entry_leadership, label_leadership],
            [entry_persuasion, label_persuasion],
            [entry_trade, label_trade],
            [entry_wander, label_wander],
            [entry_etiquette, label_etiquette],
            [entry_notice, label_notice],
            [entry_search, label_search],
            [entry_track, label_track],
            [entry_animals, label_animals],
            [entry_science, label_science],
            [entry_law, label_law],
            [entry_herballore, label_herballore],
            [entry_history, label_history],
            [entry_tactic, label_tactic],
            [entry_medicine, label_medicine],
            [entry_memorize, label_memorize],
            [entry_navigation, label_navigation],
            [entry_occult, label_occult],
            [entry_appraisal, label_appraisal],
            [entry_magic_appraisal, label_magic_appraisal],
            [entry_composure, label_composure],
            [entry_feats_of_strenght, label_feats_of_strenght],
            [entry_withstand_pain, label_withstand_pain],
            [entry_lock_picking, label_lock_picking],
            [entry_disguise, label_disguise],
            [entry_hide, label_hide],
            [entry_theft, label_theft],
            [entry_stealth, label_stealth],
            [entry_trap_lore, label_trap_lore],
            [entry_poisons, label_poisons],
            [entry_art, label_art],
            [entry_dance, label_dance],
            [entry_forging, label_forging],
            [entry_runes, label_runes],
            [entry_alchemy, label_alchemy],
            [entry_animism, label_animism],
            [entry_music, label_music],
            [entry_sleight_of_hand, label_sleight_of_hand],
            [entry_ritual, label_ritual],
            [entry_goldsmith, label_goldsmith],
            [entry_making, label_making],
            [entry_puppets, label_puppets],
            [entry_life_points_total, label_life_points_total],
            [entry_life_points_current, label_life_points_current],
            [entry_fatigue_points_total, label_fatigue_points_total],
            [entry_fatigue_points_current, label_fatigue_points_current],
            [entry_attack_base, {'text':'label_attack_base'}],
            [entry_attack_bonus, {'text':'label_attack_bonus'}],
            [entry_attack_penalizer, {'text':'label_attack_penalizer'}],
            [entry_defense_base, {'text':'label_defense_base'}],
            [entry_defense_bonus, {'text':'label_defense_bonus'}],
            [entry_defense_penalizer, {'text':'label_defense_penalizer'}],
            [entry_initiative, label_initiative],
            [entry_armor, label_armor],
            [entry_damage, label_damage],
            [entry_quality, label_quality],
            [entry_base_presence, label_base_presence],
            [entry_physical_resistance, label_physical_resistance],
            [entry_disease_resistance, label_disease_resistance],
            [entry_venom_resistance, label_venom_resistance],
            [entry_magic_resistance, label_magic_resistance],
            [box_personality, label_personality],
            [box_char_history, label_char_history],
            [box_combat_equipment, label_combat_equipment],
            [box_varied_equipment, label_varied_equipment],
            [box_advantages, label_advantages],
            [box_disadvantages, label_disadvantages]
        ]


    # Limpiar ficha
    if (es_nueva_ficha):
        # Para cada atributo (Entry), dejar vacía la casilla
        card_manager.se_abrio_nuevo_pj = True

        for atributo in card_manager.lista_entrys_y_labels:
            if isinstance(atributo[0], Entry):
                atributo[0].insert(0, "")
            elif isinstance(atributo[0], Text):
                atributo[0].insert(END,"")


    def al_cerrar_ventana():
        # Cuando se cierre la ventana de personajes, se vuelve a activar
        # el evento que responde a seleccionar elementos del listbox
        card_manager.referencia_listbox.bind('<<ListboxSelect>>', 
                lambda event: card_manager.abrir_personaje(list_box=card_manager.referencia_listbox))

        # Comando para destruir la ventana
        topCard.destroy()

    # Comando para activar una funcion al intentar cerrar la ventana de crear personaje
    topCard.protocol("WM_DELETE_WINDOW", al_cerrar_ventana)
    