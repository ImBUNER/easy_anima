from tkinter import LEFT, RAISED, IntVar, OptionMenu, StringVar, Toplevel, Label, Entry, Button, Frame
from PIL import Image, ImageTk
import calculator_backend as logic

# Ventana calculadora
def calc():
    topCalc = Toplevel()
    topCalc.title('calculadora de combate - Easy Anima')
    topCalc.geometry('860x560')
    topCalc.resizable(0, 0)
    topCalc.config(bg="#3290F1")

    #Imagen personaje 1
    player_1 = Image.open("static/player_1.png")
    player_1 = player_1.resize((250, 250), Image.ANTIALIAS)
    player_1 = ImageTk.PhotoImage(player_1)
    player_1_label = Label(topCalc, image=player_1, bg="#3290F1")
    player_1_label.image = player_1
    player_1_label.grid(column=0, row=0)

    #Imagen personaje 2
    player_2 = Image.open("static/player_2.png")
    player_2 = player_2.resize((250, 250), Image.ANTIALIAS)
    player_2 = ImageTk.PhotoImage(player_2)
    player_2_label = Label(topCalc, image=player_2, bg="#3290F1")
    player_2_label.image = player_2
    player_2_label.grid(column=0, row=1)

    #Imagen versus
    versus = Image.open("static/versus.png")
    versus = versus.resize((100, 80), Image.ANTIALIAS)
    versus = ImageTk.PhotoImage(versus)
    versus_label = Label(topCalc, image=versus, bg="#3290F1")
    versus_label.image = versus
    versus_label.place(x=300, y=210)

    #Explicacion para el usuario
    explication_zone = Frame(topCalc, pady=5, bg="#3290F1")
    explication_zone.place(x=20, y=480)
    explication = Label(explication_zone, bg="#3290F1", wraplength=700, height="5", width="92", text="Esta calculadora permite calcular ataques y defensas entre los dos personajes que se muestran. \nLos campos deben rellenarse para que funcione.")
    explication.config(justify=LEFT)
    explication.pack()

    # Contenedor resultado 
    result_zone = Frame(topCalc)
    result_zone.place(x=560, y=10)
    result_label = Label(result_zone, bd="4", relief=RAISED, wraplength=240, height="28", width="34", bg='black', fg='white')
    result_label.pack()

    # Variables de los entries
    ha_1 = IntVar()
    bonus_ha_1 = IntVar()
    penalizer_ha_1 = IntVar()
    hd_1 = IntVar()
    bonus_hd_1 = IntVar()
    penalizer_hd_1 = IntVar()
    armor_1 = IntVar()
    damage_1 = IntVar()
    quality_1 = IntVar()
    
    ha_2 = IntVar()
    bonus_ha_2 = IntVar()
    penalizer_ha_2 = IntVar()
    hd_2 = IntVar()
    bonus_hd_2 = IntVar()
    penalizer_hd_2 = IntVar()
    armor_2 = IntVar()
    damage_2 = IntVar()
    quality_2 = IntVar()

    # Recoger los valores de los inputs
    def get_data():
        logic.pj_1.ha=ha_1.get()
        logic.pj_1.bonus_ha=bonus_ha_1.get()
        logic.pj_1.penalizer_ha=penalizer_ha_1.get()
        logic.pj_1.hd=hd_1.get()
        logic.pj_1.bonus_hd=bonus_hd_1.get()
        logic.pj_1.penalizer_hd=penalizer_hd_1.get()
        logic.pj_1.armor=armor_1.get()
        logic.pj_1.damage=damage_1.get()
        logic.pj_1.quality=quality_1.get()

        logic.pj_2.ha=ha_2.get()
        logic.pj_2.bonus_ha=bonus_ha_2.get()
        logic.pj_2.penalizer_ha=penalizer_ha_2.get()
        logic.pj_2.hd=hd_2.get()
        logic.pj_2.bonus_hd=bonus_hd_2.get()
        logic.pj_2.penalizer_hd=penalizer_hd_2.get()
        logic.pj_2.armor=armor_2.get()
        logic.pj_2.damage=damage_2.get()
        logic.pj_2.quality=quality_2.get()

    
    # Datos personaje 1 -------------------------------------------
    # Ataque pj1 --------------------------------------------------
    label_ha_1 = Label(topCalc, text='HA', bg="#3290F1").place(x=252, y=40)
    entry_ha_1 = Entry(topCalc, textvariable=ha_1, bg="#f2f2f2").place(x=250, y=55, width=60, height=30)

    label_bonus_ha_1 = Label(topCalc, text='Bono', bg="#3290F1").place(x=322, y=40)
    entry_bonus_ha_1 = Entry(topCalc, textvariable=bonus_ha_1, bg="#f2f2f2").place(x=320, y=55, width=60, height=30)

    label_penalizer_ha_1 = Label(topCalc, text='Penaliz.', bg="#3290F1").place(x=392, y=40)
    entry_penalizer_ha_1 = Entry(topCalc, textvariable=penalizer_ha_1, bg="#f2f2f2").place(x=390, y=55, width=60, height=30)

    # Defensa pj1 ----------
    label_hd_1 = Label(topCalc, text='HD', bg="#3290F1").place(x=252, y=90)
    entry_hd_1 = Entry(topCalc, textvariable=hd_1, bg="#f2f2f2").place(x=250, y=105, width=60, height=30)

    label_bonus_hd_1 = Label(topCalc, text='Bono', bg="#3290F1").place(x=322, y=90)
    entry_bonus_hd_1 = Entry(topCalc, textvariable=bonus_hd_1, bg="#f2f2f2").place(x=320, y=105, width=60, height=30)

    label_penalizer_hd_1 = Label(topCalc, text='Penaliz.', bg="#3290F1").place(x=392, y=90)
    entry_penalizer_hd_1 = Entry(topCalc, textvariable=penalizer_hd_1, bg="#f2f2f2").place(x=390, y=105, width=60, height=30)

    # Equipamiento pj1 ----------
    label_armor_1 = Label(topCalc, text='TA', bg="#3290F1").place(x=252, y=140)
    entry_armor_1 = Entry(topCalc, textvariable=armor_1, bg="#f2f2f2").place(x=250, y=155, width=60, height=30)

    label_damage_1 = Label(topCalc, text='Daño', bg="#3290F1").place(x=322, y=140)
    entry_damage_1 = Entry(topCalc, textvariable=damage_1, bg="#f2f2f2").place(x=320, y=155, width=60, height=30)

    label_quality_1 = Label(topCalc, text='Calidad', bg="#3290F1").place(x=392, y=140)
    entry_quality_1 = Entry(topCalc, textvariable=quality_1, bg="#f2f2f2").place(x=390, y=155, width=60, height=30)

    # ¿CÓMO ACCEDER A EL VALOR ELEGIDO PARA USARLO?
    # quality = [
    #     "-15",
    #     "-10",
    #     "-5",
    #     "0",
    #     "+5",
    #     "+10",
    #     "+15"
    # ]
    # clicked = StringVar()
    # clicked.set(quality[3])
    # menu_quality = OptionMenu(topCalc, clicked, *quality)
    # menu_quality.place(x=390, y=155, width=60, height=30)

    # ESTO AYUDARÍA A TENER SOLO UNA FUNCIÓN DONDE ELEGIR LA ACCIÓN, Y ESTABLECER ATACANTES Y DEFENSORES EN LUGAR DE UNA PARA CADA BOTÓN
    # ¿POR QUÉ NO COGE LAS VARIABLES QUE LE PASO?
    # def combat(atacker, defender, action):
    #     get_data()
    #     result=logic.atacker.action(logic.defender)
    #     result_label.config(text=result)

    # Botones pj1 ----------
    def atack_1():
        get_data()
        result=logic.pj_1.atack(logic.pj_2)
        result_label.config(text=result)
    btn_atack_1 = Button(topCalc, text="Atacar", cursor="plus", bg="black", fg="orange", activebackground='#BDBDBD', command=atack_1)
    btn_atack_1.place(x=460, y=75, width=80, height=30)

    def defense_1():
        get_data()
        result=logic.pj_1.defend(logic.pj_2)
        result_label.config(text=result)
    btn_defense_1 = Button(topCalc, text="Defender", cursor="plus", bg="black", fg="orange", activebackground='#BDBDBD', command=defense_1)
    btn_defense_1.place(x=460, y=125, width=80, height=30)
    

    # Datos personaje 2 -------------------------------------------------
    # Ataque pj2 --------------------------------------------------------
    label_ha_2 = Label(topCalc, text='HA', bg="#3290F1").place(x=252, y=310)
    entry_ha_2 = Entry(topCalc, textvariable=ha_2, bg="#f2f2f2").place(x=250, y=325, width=60, height=30)

    label_bonus_ha_2 = Label(topCalc, text='Bono', bg="#3290F1").place(x=322, y=310)
    entry_bonus_ha_2 = Entry(topCalc, textvariable=bonus_ha_2, bg="#f2f2f2").place(x=320, y=325, width=60, height=30)

    label_penalizer_ha_2 = Label(topCalc, text='Penaliz.', bg="#3290F1").place(x=392, y=310)
    entry_penalizer_ha_2 = Entry(topCalc, textvariable=penalizer_ha_2, bg="#f2f2f2").place(x=390, y=325, width=60, height=30)
    
    # Defensa pj2 ---------
    label_hd_2 = Label(topCalc, text='HD', bg="#3290F1").place(x=252, y=360)
    entry_hd_2 = Entry(topCalc, textvariable=hd_2, bg="#f2f2f2").place(x=250, y=375, width=60, height=30)

    label_bonus_hd_2 = Label(topCalc, text='Bono', bg="#3290F1").place(x=322, y=360)
    entry_bonus_hd_2 = Entry(topCalc, textvariable=bonus_hd_2, bg="#f2f2f2").place(x=320, y=375, width=60, height=30)

    label_penalizer_hd_2 = Label(topCalc, text='Penaliz.', bg="#3290F1").place(x=392, y=360)
    entry_penalizer_hd_2 = Entry(topCalc, textvariable=penalizer_hd_2, bg="#f2f2f2").place(x=390, y=375, width=60, height=30)

    # Equipamiento pj2 ------
    label_armor_2 = Label(topCalc, text='TA', bg="#3290F1").place(x=252, y=410)
    entry_armor_2 = Entry(topCalc, textvariable=armor_2, bg="#f2f2f2").place(x=250, y=425, width=60, height=30)

    label_damage_2 = Label(topCalc, text='Daño', bg="#3290F1").place(x=322, y=410)
    entry_damage_2 = Entry(topCalc, textvariable=damage_2, bg="#f2f2f2").place(x=320, y=425, width=60, height=30)

    label_quality_2 = Label(topCalc, text='Calidad', bg="#3290F1").place(x=392, y=410)
    entry_quality_2 = Entry(topCalc, textvariable=quality_2, bg="#f2f2f2").place(x=390, y=425, width=60, height=30)

    # Botones pj2 ---------
    def atack_2():
        get_data()
        result=logic.pj_2.atack(logic.pj_1)
        result_label.config(text=result)
    btn_atack_2 = Button(topCalc, text="Atacar", cursor="plus", bg="black", fg="cyan", activebackground='#BDBDBD', command=atack_2)
    btn_atack_2.place(x=460, y=350, width=80, height=30)

    def defense_2():
        get_data()
        result=logic.pj_2.defend(logic.pj_1)
        result_label.config(text=result)
    btn_defense_2 = Button(topCalc, text="Defender", cursor="plus", bg="black", fg="cyan", activebackground='#BDBDBD', command=defense_2)
    btn_defense_2.place(x=460, y=400, width=80, height=30)

