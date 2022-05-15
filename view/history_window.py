from tkinter import EXTENDED, LEFT, RIGHT, VERTICAL, Y, Button, Entry, Listbox, Scrollbar, StringVar, Toplevel, Frame
import history_manager

# When "counter" is True, allow to open the history
global counter
counter = True

def open_history_box():
    global counter
    if counter:
        topHistory = Toplevel()
        topHistory.title("Historial de tiradas - Easy Anima")
        topHistory.geometry("300x1000")
        topHistory.resizable(0, 0)
        counter = False

        history_frame = Frame(topHistory)

        scroll = Scrollbar(history_frame, orient=VERTICAL)

        # Content where put the items 
        history_box = Listbox(
            history_frame,
            yscrollcommand=scroll.set,
            borderwidth=0,
            bg="black",
            fg="white",
            highlightthickness=0,
            selectbackground="#3290F1",
            font=10,
            selectmode=EXTENDED,
            )

        history_manager.history_box = history_box
        history_manager.llenar_historial()

        scroll.config(command=history_box.yview)
        scroll.pack(side=RIGHT, fill=Y)

        history_frame.pack(fill="both", expand=1)
        history_box.pack(fill="both", expand=1)  

        manual_item = StringVar()
        manual_entry = Entry(history_frame, textvariable=manual_item, width=29)
        manual_entry.pack(side=LEFT, fill=Y)


        btn_clean = Button(
            history_frame,
            text="Limpiar",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=lambda:history_manager.alterar_historial(
                tipo_de_modificacion='clean',
                )
        )
        btn_clean.place(x=200, y=850)

        btn_delete = Button(
            history_frame,
            text="Eliminar",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=lambda:history_manager.alterar_historial(
                tipo_de_modificacion='delete',
                )
        )
        btn_delete.place(x=200, y=900)

        btn_add = Button(
            history_frame,
            text="Add",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=lambda: history_manager.alterar_historial(
                tipo_de_modificacion='add from bar',
                manual_item=manual_item)
        )
        btn_add.pack(side=RIGHT)


        def al_cerrar_history():
            global counter
            counter=True
            topHistory.destroy()

        # Comando para activar una funcion al intentar cerrar la ventana de crear personaje
        topHistory.protocol("WM_DELETE_WINDOW", al_cerrar_history)
