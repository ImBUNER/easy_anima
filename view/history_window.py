from pickle import FRAME
from tkinter import ANCHOR, END, EXTENDED, LEFT, RIGHT, VERTICAL, Y, Button, Entry, Listbox, Scrollbar, StringVar, Toplevel, Frame

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
 

        scroll.config(command=history_box.yview)
        scroll.pack(side=RIGHT, fill=Y)

        history_frame.pack(fill="both", expand=1)
        history_box.pack(fill="both", expand=1)  





        manual_item = StringVar()
        manual_entry = Entry(history_frame, textvariable=manual_item, width=29)
        manual_entry.pack(side=LEFT, fill=Y)

        btn_close = Button(
            history_frame,
            text="Cerrar",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=lambda:[topHistory.destroy(), counter_on()] 
        )
        btn_close.place(x=210, y=800)


        btn_clean = Button(
            history_frame,
            text="Limpiar",
            cursor="fleur",
            bg="black",
            fg="white",
            activeforeground="black",
            activebackground="#BDBDBD",
            command=lambda:history_box.delete(0, END) 
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
            command=lambda:history_box.delete(ANCHOR)
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
            command=lambda: history_box.insert(0, manual_item.get())
        )
        btn_add.pack(side=RIGHT)

    



