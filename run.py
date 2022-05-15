# I'm BUNER
from tkinter import Tk
import view.main_window as main
import os
import card_manager
import history_manager

if __name__ == "__main__":

    if not os.path.exists(card_manager.dirName):
        os.mkdir(card_manager.dirName)

    if not os.path.exists(history_manager.history_file):
        with open(history_manager.history_file, 'w'):
            pass

    card_manager.cargar_pjs_a_memoria()

    root = Tk()
    application = main.app(root)
    root.mainloop()
