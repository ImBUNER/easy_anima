from tkinter import ANCHOR, END, LEFT, RIGHT, VERTICAL, Y, Button, Entry, Listbox, Scrollbar, StringVar, Toplevel, messagebox

# When "counter" is True, allow to open the history
global counter
counter = True

# Swap to "True" the counter
def counter_on():
    global counter
    counter=True

def open():
    global counter
    if counter:
        topHistory = Toplevel()
        topHistory.title("Historial de tiradas - Easy Anima")
        topHistory.geometry("300x1000")
        topHistory.resizable(0, 0)
        counter = False

        scroll = Scrollbar(topHistory, orient=VERTICAL)

        # Content when the items place
        history_box = Listbox(
            topHistory,
            yscrollcommand=scroll.set,
            borderwidth=0,
            bg="black",
            fg="white",
            highlightthickness=0,
            selectbackground="#3290F1",
            font=10,

            )
        history_box.pack(fill="both", expand=1)   

        scroll.config(command=history_box.yview)
        scroll.pack(side=RIGHT, fill=Y)

        manual_item = StringVar()
        manual_entry = Entry(topHistory, textvariable=manual_item)
        manual_entry.pack(side=LEFT)












        btn_close = Button(
            topHistory,
            text="Cerrar",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=lambda:[topHistory.destroy(), counter_on()] 
        )
        btn_close.place(x=210, y=10)


        btn_clean = Button(
            topHistory,
            text="Limpiar",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=lambda:history_box.delete(0, END) 
        )
        btn_clean.place(x=210, y=50)


        btn_insert = Button(
            topHistory,
            text="Testear",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=lambda:history_box.insert(0, "  testing...") 
        )
        btn_insert.place(x=210, y=100)

        btn_delete = Button(
            topHistory,
            text="Eliminar",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=lambda:history_box.delete(ANCHOR)
        )
        btn_delete.place(x=210, y=150)

        btn_add = Button(
            topHistory,
            text="Add",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=lambda: history_box.insert(0, manual_item.get())
        )
        btn_add.place(x=210, y=500)

    



