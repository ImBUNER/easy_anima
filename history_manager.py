from tkinter import ANCHOR, END, messagebox
import view.history_window
import view.card_window
import card_manager
import dice_manager
import os

history_file = './history.txt'
history_box = None

def llenar_historial():
    global history_box
    # Si el archivo del historial existe
    if os.path.exists(history_file):
        # Abrirlo para lectura
        with open(history_file, 'r') as f:
            # Iterar sobre cada linea del archivo
            for line in f.readlines():
                # Llenar el history_box con el contenido del archivo
                history_box.insert(END, line.strip())


def guardar_historial_en_archivo():
    global history_box
    listbox_items = history_box.get(0, END)
    with open(history_file, 'w') as f:
        for item in listbox_items:
            f.write(f'{item}\n')


# Funcion que se ejecuta cada vez que se modifique el historial
def alterar_historial(tipo_de_modificacion,  
                        manual_item=None):
    global history_box

    view.history_window.open_history_box()

    # Activada al presionar Add en el history box
    if tipo_de_modificacion == 'add from bar':
        history_box.insert(0, manual_item.get())


    # Activada al presionar Eliminar en el history box
    elif tipo_de_modificacion == 'delete':
        history_box.delete(ANCHOR)


    # Activada al presionar Limpiar en el history box
    elif tipo_de_modificacion == 'clean':
        history_box.delete(0, END) 


    # Activada al presionar Turno en el en la ventana de personaje
    elif tipo_de_modificacion == 'turno':
        
        valor_casilla = view.card_window.page_1.nametowidget("turno").get()

        if valor_casilla.isdigit():
            valor_casilla = int(valor_casilla) + dice_manager.roll(100)
            history_box.insert(0, f'{card_manager.nombre_pj.split(" - ")[0]} - Turno [{valor_casilla}]')
            print('turno')

        else:
            messagebox.showerror(title="ERROR", message=(f'El valor de la casilla {tipo_de_modificacion} debe ser un numero'))


    elif tipo_de_modificacion == 'caracteristica':
        # En esta variable se debe capturar la selección del dropmenu para caracteristica
        dropmenu_caract = view.card_window.caracteristic.get()
        valor_casilla = view.card_window.page_1.nametowidget(dropmenu_caract).get()

        if valor_casilla.isdigit():
            valor_casilla = int(valor_casilla) + dice_manager.roll(10)
            history_box.insert(0, f'{card_manager.nombre_pj.split(" - ")[0]} - {dropmenu_caract.upper()} [{valor_casilla}]')

        else:
            messagebox.showerror(message=(f'El valor de la casilla {tipo_de_modificacion} debe ser un numero'))


    elif tipo_de_modificacion == 'combate':
        # En esta variable se debe capturar la selección del dropmenu para combate
        dropmenu_combate = view.card_window.combat.get()

        if dropmenu_combate == "Ataque":
            base = view.card_window.page_1.nametowidget('atk-base').get()
            bonus = view.card_window.page_1.nametowidget('atk-bonus').get()
            penalizer = view.card_window.page_1.nametowidget('atk-penalizer').get()

            if not base.isdigit() or not bonus.isdigit() or not penalizer.isdigit():
                messagebox.showerror(message=(f"Los valores de {dropmenu_combate} deben ser numericos"))
                return
        
        elif dropmenu_combate == 'Defensa':
            base = view.card_window.page_1.nametowidget('def-base').get()
            bonus = view.card_window.page_1.nametowidget('def-bonus').get()
            penalizer = view.card_window.page_1.nametowidget('def-penalizer').get()

            if not base.isdigit() or not bonus.isdigit() or not penalizer.isdigit():
                messagebox.showerror(message=(f"Los valores de {dropmenu_combate} deben ser numericos"))
                return


        valor_casilla = int(base) + int(bonus) - int(penalizer) + dice_manager.roll(100)

        history_box.insert(0, f'{card_manager.nombre_pj.split(" - ")[0]} - {dropmenu_combate} [{valor_casilla}]')


    elif tipo_de_modificacion == 'secundarias':
        # En esta variable se debe capturar la selección del dropmenu para secundarias
        dropmenu_secund = view.card_window.secondary.get().lower()
        valor_casilla = view.card_window.page_1.nametowidget(dropmenu_secund).get()

        if valor_casilla.isdigit():
            valor_casilla = int(valor_casilla) + dice_manager.roll(100)
            history_box.insert(0, f'{card_manager.nombre_pj.split(" - ")[0]} - {dropmenu_secund.title()} [{valor_casilla}]')

        else:
            messagebox.showerror(message=(f'El valor de la casilla {tipo_de_modificacion} debe ser un numero'))
    

    elif tipo_de_modificacion == 'resistencias':
        # En esta variable se debe capturar la selección del dropmenu para resistencias
        dropmenu_resis = view.card_window.resistence.get()
        print(dropmenu_resis)
        valor_casilla = view.card_window.page_1.nametowidget(dropmenu_resis).get()

        if valor_casilla.isdigit():
            valor_casilla = int(valor_casilla) + dice_manager.roll(100)
            history_box.insert(0, f"{card_manager.nombre_pj.split(' - ')[0]} - {dropmenu_resis.title()} [{valor_casilla}]")

        else:
            messagebox.showerror(message=(f'El valor de la casilla {tipo_de_modificacion} debe ser un numero'))


    guardar_historial_en_archivo()
