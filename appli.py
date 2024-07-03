import tkinter as tk               
from tkinter import font  as tkfont
from frontend.startPage import StartPage
from frontend.menuPage import MenuPage
from frontend.afficherPage import AfficherPage
from frontend.operationPage import OperationPage
from frontend.ajouterPage import AjouterPage
from frontend.chercherPage import ChercherPage

# c'est la  classe principale pour afficher tout nos pages
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

      
        #le container est l’endroit où nous allons empiler un tas de cadres
        # les uns sur les autres, puis celui que nous voulons voir
        # sera élevé au-dessus des autres
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, AfficherPage, OperationPage, AjouterPage, ChercherPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # mettre toutes les pages au même endroit;
            # celui en haut de l’ordre d’empilement
            # sera celui qui est visible.
            #nsew  permet au frame de prendre toute la place disponible dans la cellule
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
    #methode showframe pour mettre le frame donnée au tête du container 
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
