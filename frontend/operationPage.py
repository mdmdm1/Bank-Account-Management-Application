import tkinter  as tk
from tkinter import messagebox
from tkinter import *
from backend.ConnectionDataBase import DataBase
from backend.clientDAO import ClientDAO
from backend.Operation import Operation

class OperationPage(tk.Frame):

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
                                                           text='Effectuer une operation',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#3d3d5c')
        title_label.pack()
        
        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)
        bottom_frame = tk.Frame(self, width="40px", height="60px" ,borderwidth=3)
        bottom_frame.pack(fill='both', side='top', expand=True)

        conn= DataBase.get_conn()
        conn.reconnect()
        cursor=conn.cursor()
# pour faire un transfert        
        def submitact():
            m1 = int(id1.get())
            m2 = int(id2.get())
            mo = float(montant.get())
            c1 = ClientDAO.findCompte3(m1)
            c2=ClientDAO.findCompte3(m2)
            o=Operation('virement',mo, c1).virement(c2)
            if o!=None:
                messagebox.showinfo(title="message", message="le transfert a été effectué!")
                controller.show_frame('AfficherPage')
                montant.delete(0, 'end')
                
            else:
                messagebox.showinfo(title="message", message="erreur!")
        global email
        global montant

        lblmail = tk.Label(bottom_frame, text ="Envoyer du compte: ",width = 35, borderwidth=2,relief='ridge', anchor="w" )
        lblmail.grid(row=0, column=0)

        id1 = tk.Entry(bottom_frame, width = 35)
        id1.grid(row=0, column=1)
        
        lblmail2 = tk.Label(bottom_frame, text ="vers: ",width = 35, borderwidth=2,relief='ridge', anchor="w" )
        lblmail2.grid(row=1, column=0)

        id2 = tk.Entry(bottom_frame, width = 35)
        id2.grid(row=1, column=1)

        lblsecrow = tk.Label(bottom_frame, text ="le montant  -",width = 35, borderwidth=2,relief='ridge', anchor="w")
        lblsecrow.grid(row=2, column=0)
        
        montant = tk.Entry(bottom_frame, width = 35)
        montant.grid(row=2, column=1)
        
        submitbtn = tk.Button(bottom_frame, text ="envoyer",  command = submitact)
        submitbtn.grid(row=3, column=1)
       
        
       
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

