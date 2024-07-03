from backend.ConnectionDataBase import DataBase 
import tkinter  as tk
from tkinter import messagebox
from tkinter import *
from backend.Search import Search

class ChercherPage(tk.Frame):

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
                                                           text='chercher un compte',
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
#--------------------------------- Fonction recherche       
        def chercher():
            idl = int(id.get())
            
            lblid = tk.Label(bottom_frame, text ="id", )
            lblid.grid(row=2, column=0)

            lblnom = tk.Label(bottom_frame, text ="nom", )
            lblnom.grid(row=2, column=1)

            lblprenom = tk.Label(bottom_frame, text ="prenom", )
            lblprenom.grid(row=2, column=2)

            lblemail = tk.Label(bottom_frame, text ="email", )
            lblemail.grid(row=2, column=3)

            lblsolde = tk.Label(bottom_frame, text= "solde", )
            lblsolde.grid(row=2, column=4)

            c,cm=Search().search(idl)

            idt= IntVar()
            nom=StringVar()
            prenom=StringVar()
            email=StringVar()
            solde=StringVar()
# pour 
            if c is not None:
                n= c.get_nom()
                em = c.get_email()
                pr= c.get_prenom()
                so = cm.get_solde()
                idt.set(idl)
                nom.set(n)
                prenom.set(pr)
                email.set(em)
                solde.set(so)
            else:
              
                idt.set(0)
                nom.set("!")
                prenom.set("!")
                email.set("!")
                solde.set(0000)
# Pour saisir les infomations du compte a modifier
            lblid = tk.Entry(bottom_frame, text =idt, )
            lblid.grid(row=3, column=0)

            lblnom = tk.Entry(bottom_frame, text =nom, )
            lblnom.grid(row=3, column=1)

            lblprenom = tk.Entry(bottom_frame, text =prenom, )
            lblprenom.grid(row=3, column=2)

            lblemail = tk.Entry(bottom_frame, text =email, )
            lblemail.grid(row=3, column=3)

            lblsolde = tk.Entry(bottom_frame, text= solde, )
            lblsolde.grid(row=3, column=4)
# Fonction pour mettre a jour la base de données
            def modifier():
                #controller.show_frame('ModifierPage')
                idt = lblid.get()
                c,cm=Search().search(idl)
                idCli=c.get_num()
                nom = lblnom.get()
                prenom = lblprenom.get()
                email = lblemail.get()
                solde = lblsolde.get()
                cursor=conn.cursor()
                cursor.execute(('UPDATE comptes SET soldes=%s WHERE id=%s'),(solde,idt,))
                conn.commit()
                cursor.execute(('UPDATE  client SET nom=%s,prenom=%s,email=%s WHERE id=%s'),(nom,prenom,email,idCli,))
                conn.commit()
                cursor.close()
                if c!=None:
                    messagebox.showinfo(title="message", message="La modification a été effectué!")
                    controller.show_frame('AfficherPage')
                else:
                    messagebox.showinfo(title="message", message="erreur!")
                
            afficher_button = tk.Button(bottom_frame,text='Modifier',  command=modifier,)
            afficher_button.grid(row=3,column=6)
# Pour supprimer un compte
            def supprimer():
                #controller.show_frame('SupprimerPage')
                idt = lblid.get()
                c,cm=Search().search(idl)
                idCli=c.get_num()
                cursor=conn.cursor()
                cursor.execute(('DELETE FROM comptes WHERE id=%s'),(idt,))
                conn.commit()
                cursor.execute(('DELETE FROM client  WHERE id=%s'),(idCli,))
                conn.commit()
                cursor.close()
                if c!=None:
                    messagebox.showinfo(title="message", message="La suppression a été effectué!")
                    controller.show_frame('AfficherPage')
                else:
                    messagebox.showinfo(title="message", message="erreur!")
                
            afficher_button = tk.Button(bottom_frame,text='Supprimer', command=supprimer,)
            afficher_button.grid(row=3,column=7)
        
       
#### pour recuperer donner l'id a chercher
        global id
       
        lblsecrow = tk.Label(bottom_frame, text ="Donner id comptes ")
        lblsecrow.grid(row=0,column=0)
        
        id = Entry(bottom_frame, width = 35)
        id.grid(row=0,column=1)

        submitbtn = Button(bottom_frame, text ="Confirmer", command=chercher)
        submitbtn.grid(row=0,column=2)
        
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

