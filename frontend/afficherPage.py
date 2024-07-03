from backend.ConnectionDataBase import DataBase 
import tkinter  as tk
from backend.ConnectionDataBase import DataBase
from backend.clientDAO import ClientDAO

# Page pour afficher les Clients

class AfficherPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
       
        
        heading_label = tk.Label(self,
                                                     text='Admin',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=25)

        title_label = tk.Label(self,
                                                           text='Afficher les Comptes',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#3d3d5c')
        title_label.pack()
        
        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        #bottom_frame
        
        bottom_frame = tk.Frame(self, width="400px", height="100px" ,borderwidth=3)
        bottom_frame.pack_forget
        bottom_frame.pack(fill='both', side='top', expand=True)
        

        lblid = tk.Label(bottom_frame, width=10, text ="id Comptes",borderwidth=2,relief='ridge', anchor="w" )
        lblid.grid(row=0, column=0)

        lblnom = tk.Label(bottom_frame, width=10,text ="nom",borderwidth=2,relief='ridge', anchor="w" )
        lblnom.grid(row=0, column=1)

        lblprenom = tk.Label(bottom_frame,width=10, text ="prenom",borderwidth=2,relief='ridge', anchor="w" )
        lblprenom.grid(row=0, column=2)

        lblemail = tk.Label(bottom_frame,width=25, text ="email", borderwidth=2,relief='ridge', anchor="w")
        lblemail.grid(row=0, column=3)

        lblsolde = tk.Label(bottom_frame,width=10, text= "solde", borderwidth=2,relief='ridge', anchor="w")
        lblsolde.grid(row=0, column=4)

        lbldate= tk.Label(bottom_frame,width=10, text= "date",borderwidth=2,relief='ridge', anchor="w")
        lbldate.grid(row=0, column=5)
        
        def act():
            
            
            global output
        
            conn= DataBase.get_conn()
            conn.reconnect()
            cursor=conn.cursor()        
            cursor.execute('SELECT * FROM comptes' )
            output = cursor.fetchall()
            cursor.close()
            
            l  = len(output)

            for i in range(0, l):
                i1=tk.IntVar()
                n1=tk.StringVar()
                p1=tk.StringVar()
                e1=tk.StringVar()
                s1=tk.StringVar()
                d1=tk.StringVar()

                
                idc = output[i][3]
                c = ClientDAO.findClient(idc)
                nom= c.get_nom()
                prenom= c.get_prenom()
                email = c.get_email()
                idcm=output[i][0]
                
                lblid = tk.Label(bottom_frame,width=10, text =idcm,borderwidth=2,relief='ridge', anchor="w" )
                lblid.grid(row=i+1, column=0)

                lblnom = tk.Label(bottom_frame,width=10, text=nom,borderwidth=2,relief='ridge', anchor="w" )
                lblnom.grid(row=i+1, column=1)

                lblprenom = tk.Label(bottom_frame,width=10, text=prenom, borderwidth=2,relief='ridge', anchor="w")
                lblprenom.grid(row=i+1, column=2)

                lblemail = tk.Label(bottom_frame,width=25, text =email,borderwidth=2,relief='ridge', anchor="w" )
                lblemail.grid(row=i+1, column=3)

                lblsolde = tk.Label(bottom_frame,width=10, text= output[i][1], borderwidth=2,relief='ridge', anchor="w")
                lblsolde.grid(row=i+1, column=4)

                lbldate= tk.Label(bottom_frame,width=10, text= output[i][2],borderwidth=2,relief='ridge', anchor="w")
                lbldate.grid(row=i+1, column=5)
            
            
                
        submitbtn = tk.Button(bottom_frame, text ="actualiser", command = act)
        submitbtn.grid(row=0, column=6)

        # self.change_frame()

        # def change_frame(self):
        
        
        
       
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

