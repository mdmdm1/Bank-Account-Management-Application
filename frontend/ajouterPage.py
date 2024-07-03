import tkinter  as tk
from tkinter import *
from backend.ConnectionDataBase import DataBase
from backend.Client import Client
from backend.Comptes import Comptes

# Page d'ajout

class AjouterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        global l 
        
        heading_label = tk.Label(self,
                                                     text='Admin',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=25)

        title_label = tk.Label(self,
                                                           text='Ajouter un client',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#3d3d5c')
        title_label.pack()
        
        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        #bottom_frame
        bottom_frame = tk.Frame(self, width="40px", height="60px" ,borderwidth=3)
        bottom_frame.pack(fill='both', side='top', expand=True)
        
        def submit():
            c1 = Client
            c= Comptes
            n = nom.get()
            p= prenom.get()
            md= mdp.get()
            ml= email.get()
            so= solde.get()
            c1 = Client(n, p, ml, md)
            c= Comptes(c1, so)

            if c!=None:
                tk.messagebox.showinfo(title="message", message="l'ajout a été effectué!")
                controller.show_frame('AfficherPage')
               
                
            else:
                tk.messagebox.showinfo(title="message", message="erreur!")
    
    # formulaire    

        lblid = tk.Label(bottom_frame, text ="nom",width = 10,borderwidth=2,relief='ridge', anchor="w" )
        lblid.grid(row=0, column=0)
        nom = tk.Entry(bottom_frame, width = 35,borderwidth=2,relief='ridge',)
        nom.grid(row=0, column=1)

        lblprenom = tk.Label(bottom_frame, text= "prenom",width = 10, borderwidth=2,relief='ridge', anchor="w")
        lblprenom.grid(row=1, column=0)
        prenom = tk.Entry(bottom_frame, width = 35,borderwidth=2,relief='ridge', )
        prenom.grid(row=1, column=1)

        lblemail= Label(bottom_frame, text= "email",width = 10, borderwidth=2,relief='ridge', anchor="w")
        lblemail.grid(row=2, column=0)
        email = tk.Entry(bottom_frame, width = 35,borderwidth=2,relief='ridge', )
        email.grid(row=2, column=1)

        lblmdp= tk.Label(bottom_frame, text= "Mot de passe",width = 10, borderwidth=2,relief='ridge', anchor="w")
        lblmdp.grid(row=3, column=0)
        
        mdp = tk.Entry(bottom_frame, width = 35,borderwidth=2,relief='ridge',)
        mdp.grid(row=3, column=1)

        lblsolde= tk.Label(bottom_frame, text= "Solde",width = 10, borderwidth=2,relief='ridge', anchor="w")
        lblsolde.grid(row=4, column=0)
        
        solde = tk.Entry(bottom_frame, width = 35,borderwidth=2,relief='ridge', )
        solde.grid(row=4, column=1)

        submitbtn = Button(bottom_frame, text ="Ajouter", command=submit)
        submitbtn.grid(row=6, column=1)
        
        
        def afficher():
            controller.show_frame('AfficherPage')
                
        afficher_button = tk.Button(button_frame,
                                                                text='Afficher',
                                                            command=afficher,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=40,
                                                            height=5)
        afficher_button.grid(row=0,column=0,pady=4)

        def ajouter():
            controller.show_frame('AjouterPage')
            
        ajouter_button = tk.Button(button_frame,
                                                            text='Ajouter',
                                                            command=ajouter,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=40,
                                                            height=5)
        ajouter_button.grid(row=0,column=1,pady=4)

        def operation():
            controller.show_frame('OperationPage')
            
        operation_button = tk.Button(button_frame,
                                                            text='Operation',
                                                            command=operation,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=40,
                                                            height=5)
        operation_button.grid(row=0,column=2,pady=4)

        def search():
            controller.show_frame('ChercherPage')
            
        search_button = tk.Button(button_frame,
                                                            text='Search',
                                                            command=search,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=40,
                                                            height=5)
        search_button.grid(row=0,column=3,pady=4)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,
                                                            text='Exit',
                                                            command=exit,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=40,
                                                            height=5)
        exit_button.grid(row=0,column=4,pady=4)

