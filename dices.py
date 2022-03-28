from tkinter import Toplevel, Label, Button
import random

# Ventana Dados
def roll():
    topDice = Toplevel()
    topDice.title('dados - Easy Anima')
    topDice.geometry('400x250')
    topDice.resizable(0, 0)
    topDice.config(bg="#3290F1")

    # Función que realiza la tirada de los dados ("max" es el resultado más alto que puede salir en los dados)
    def roll_dice(max):
        result=random.randint(1,max)
        if result < 90:
            label.configure(text=result)
            label.pack()
        else:
            result=result+random.randint(1,100)
            label.configure(text=result)
            label.pack()

    # Contenedor donde mostrar el resultado
    label = Label(topDice, font=("comic sans ms", 120), width=10, pady=10, bg="#3290F1")

    # Botones de los dados
    d2_btn = Button(topDice, text='D2', cursor="pirate", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', command=lambda:roll_dice(2))
    d2_btn.place(relx= 0.2, rely=0.75, anchor='center')

    d3_btn = Button(topDice, text='D3', cursor="pirate", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', command=lambda:roll_dice(3))
    d3_btn.place(relx= 0.4, rely=0.75, anchor='center')
    
    d4_btn = Button(topDice, text='D4', cursor="pirate", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', command=lambda:roll_dice(4))
    d4_btn.place(relx= 0.6, rely=0.75, anchor='center')
    
    d6_btn = Button(topDice, text='D6', cursor="pirate", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', command=lambda:roll_dice(6))
    d6_btn.place(relx= 0.8, rely=0.75, anchor='center')
    
    d10_btn = Button(topDice, text='D10', cursor="pirate", bg="white", fg="black", activeforeground="black", activebackground='#BDBDBD', command=lambda:roll_dice(10))
    d10_btn.place(relx= 0.2, rely=0.9, anchor='center')
    
    d12_btn = Button(topDice, text='D12', cursor="pirate", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', command=lambda:roll_dice(12))
    d12_btn.place(relx= 0.4, rely=0.9, anchor='center')
    
    d20_btn = Button(topDice, text='D20', cursor="pirate", bg="black", fg="white", activeforeground="black", activebackground='#BDBDBD', command=lambda:roll_dice(20))
    d20_btn.place(relx= 0.6, rely=0.9, anchor='center')

    d100_btn = Button(topDice, text='D100', cursor="pirate", bg="white", fg="black", activeforeground="black", activebackground='#BDBDBD', command=lambda:roll_dice(100))
    d100_btn.place(relx= 0.8, rely=0.9, anchor='center')