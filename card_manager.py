import os
from pathlib import Path
import glob
import view.card_window
from tkinter import END, INSERT, Entry, Text
import re

# Variables globales del programa
id_ultimo_pj_creado = 0    # Se almacena el ID mas alto de los archivos
personaje_seleccionado = -1    # Que personaje se encuentra seleccionado (-1 indica que ninguno)
cantidad_personajes = 0    # Cuantos personajes (archivos) hay
dirName = './character_cards'    # Carpeta donde se encuentran los archivos de pj
lista_entrys_y_labels = []  # Lista con todos los entry y labels widgets de la vista de character_window
lista_archivos_pj = []  # Lista de todos los nombres de los archivos
dicc_de_pjs = {}    # Diccionario donde cada llave es un pj y el valor es un diccionario con todos los atributos
referencia_listbox = None   # Variable para almacenar la referencia del listobox de main_window y usarla en otras partes
se_abrio_nuevo_pj = False
nombre_pj = ''


# Funcion se ejecuta al inicio del programa
def cargar_pjs_a_memoria():
    global lista_archivos_pj, id_ultimo_pj_creado, cantidad_personajes
    # Buscar en la carpeta todos los archivos que tengan el formato adecuado de acuerdo al regex
    # y devuelve una lista con los sus nombres
    lista_archivos_pj = [Path(f).stem for f in glob.glob(f"{dirName}/ID_[0-9]*.txt")]

    # Calcular cuantos personajes hay con base en la cantidad de archivos
    cantidad_personajes = len(lista_archivos_pj)

    # No hay personajes, el primer ID es 0
    if cantidad_personajes == 0:
        id_ultimo_pj_creado = 0

    # Caso contrario: Hay al menos 1 personaje - achivo creado
    else:
        # organizar los archivos por su nombre
        lista_archivos_pj.sort()
        # Mirar cual es el ID mas grande que hay entre lso archivos
        id_ultimo_pj_creado = int(re.findall(r'ID_(\d+)', lista_archivos_pj[-1])[0])

        # Para cada archivo
        for archivo in lista_archivos_pj:
            # Abrir el archivo
            with open(f'{dirName}/{archivo}.txt', 'r') as f:
                # Crear un diccionario vacío donde se almacenará
                # la información del pj
                datos_pj = {}
                # Por cada atributo encontrado en el archivo
                for atributo in f.readlines():
                    # Dividir el atributo y valor en una tupla
                    line = atributo.split("=")
                    # Separar en 2 variables el atributo (key) y su valor (value)
                    key = line[0].strip()
                    value = line[1].strip()
                    # Agregar al diccionario el atributo con su valor
                    datos_pj[key] = value

            # Agregar al diccionario de personajes la informacion del
            # personaje añadido
            dicc_de_pjs[archivo] = datos_pj



def cargar_personajes_en_listbox(list_box):
    global lista_archivos_pj, dirName
    # Borar todo el listbox
    list_box.delete(0, END)
    
    # Por cada archivo encontrado en personajes
    for archivo in lista_archivos_pj:
        # Abrir el archivo
        with open(f'{dirName}/{archivo}.txt', 'r') as f:
            # Extraer el primer atributo, el nombre del personaje
            atributo_nombre = f.readlines()[0]
            # Dividir entre el nombre del aributo y el valor
            line = atributo_nombre.split("=")
            # Guardar el apodo del personaje y concatenarle el nombre del archivo (ID_X)
            apodo = f'{line[1].strip()} - {archivo}'
            # Agregar la variable al listbox
            list_box.insert(END, apodo)




def abrir_personaje(list_box):
    global personaje_seleccionado, se_abrio_nuevo_pj, referencia_listbox, nombre_pj

    # Al abrir el personaje, desactivar el evento de dar click en las opciones
    referencia_listbox.bind('<<ListboxSelect>>', lambda event: None)
    
    # Si esta funcion es llamada desde el boton de nuevo pj, list_box será none
    if list_box == None:
        view.card_window.open(es_nueva_ficha=True)
        se_abrio_nuevo_pj = True

    else:
        # Al seleccionar un elemento del listbox, se crea una tupla con 1 solo elemento
        tupla_seleccionados = list_box.curselection()

        # Si se seleccionó al menos un personaje (doble comprobacion)
        if len(tupla_seleccionados) > 0:

            # Se obtiene el index en el listbox de ese personaje (su index real es con +1)
            pj_en_index = int(list_box.curselection()[0])

            # El nombre del personaje del listbox obtenido con el index
            nombre_pj = list_box.get(pj_en_index)
            
            # Buscar cual es el ID del personaje seleccionado
            personaje_seleccionado = int(re.findall(r'ID_(\d+)', nombre_pj)[0])
            # Del diccionario de pjs, se busca el que tenga el nombre seleccionado del listbox
            datos_pj = dicc_de_pjs[f'ID_{personaje_seleccionado}']
            
            # Se abre la ventana de caracter
            view.card_window.open(es_nueva_ficha=False)
            # Se cambia el titulo de la ventana de personaje
            view.card_window.topCard.title(f'{nombre_pj.split(" - ")[0]} - Easy Anima')

            # Se llenan los atributos utilizando el diccionario del personaje
            # Se llama cada entry o textbox y se llena con la información
            for index, atributo in enumerate(datos_pj):
                
                if isinstance(lista_entrys_y_labels[index][0], Entry):
                    lista_entrys_y_labels[index][0].insert(0, datos_pj[atributo])

                elif isinstance(lista_entrys_y_labels[index][0], Text):
                    box_string = '\n'.join(datos_pj[atributo].split("||"))
                    lista_entrys_y_labels[index][0].insert(INSERT, box_string) 




def eliminar_personaje(referencia_ventana_pj):
    global personaje_seleccionado
    
    # Si no hay personaje seleccionado, acabar la funcion (comprobacion)
    if personaje_seleccionado == -1:
        return

    # Borrar el archivo con el ID del personaje seleccionado
    os.remove(f"{dirName}/ID_{personaje_seleccionado}.txt")

    # Cuando se cierre la ventana de personajes, se vuelve a activar
    # el evento que responde a seleccionar elementos del listbox
    referencia_listbox.bind('<<ListboxSelect>>', 
            lambda event: abrir_personaje(list_box=referencia_listbox))

    # Una vez borrado el archivo, deseleccionar personaje
    personaje_seleccionado = -1
    cargar_pjs_a_memoria()
    cargar_personajes_en_listbox(referencia_listbox)
    # Cerrar ventana de personaje
    referencia_ventana_pj.destroy()




def guardar_personaje(lista_entry_labels):
    global personaje_seleccionado, referencia_listbox, cantidad_personajes, se_abrio_nuevo_pj, nombre_pj

    # Se busca el nombre del pj que está en el widget con atributo name="nombre_pj"
    nombre_pj = view.card_window.page_2.nametowidget("nombre_pj").get()
    view.card_window.topCard.title(f'{nombre_pj} - Easy Anima')

    if se_abrio_nuevo_pj == True:
        nombre_archivo = f'{dirName}/ID_{id_ultimo_pj_creado + 1}.txt'
        se_abrio_nuevo_pj = False
    else:
        nombre_archivo = f'{dirName}/ID_{personaje_seleccionado}.txt'  

    # Crear archivo con la información de los personajes o edita el existente
    with open(nombre_archivo, 'w') as archivo_personaje:
        # Por cada par de widgets (entry o text, y label)
        for widget in lista_entry_labels:
            # Comprobar si es un entry o text para guardar el valor
            if isinstance(widget[0], Entry):
                valor = widget[0].get()
            elif isinstance(widget[0], Text):
                valor = widget[0].get("1.0",'end-1c')
                valor = '||'.join(valor.split("\n"))

            # Acceder a la propiedad text del label para almacenarlo
            # como nombre del atributo
            label = widget[1]['text']
            # Escribir linea a linea el nobre del atributo
            archivo_personaje.write(f'{label} = {valor}\n')
        
        
    # Actualizar diccionario personaje
    cargar_pjs_a_memoria()

    tupla_seleccionados = referencia_listbox.curselection()
    
    if len(tupla_seleccionados) == 0 and personaje_seleccionado == -1:
        personaje_seleccionado = id_ultimo_pj_creado
    
    # Actualizar listbox
    cargar_personajes_en_listbox(referencia_listbox)
