from backend.clientDAO import ClientDAO
from backend.ConnectionDataBase import DataBase 
import tkinter  as tk




class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        self.controller.title('BANK')
        self.controller.state('zoomed')
    # c'est l'entête de la page start page (BANK SYSTEM)
        heading_label = tk.Label(self,
                                                     text='BANK SYSTEM',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=25)

#-------------------------------------------------------------------------------------------
# Assuthentification
        space_label = tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()

        
        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        email_label = tk.Label(self,
                                                      text='Email',
                                                      font=('orbitron',13),
                                                      bg='#3d3d5c',
                                                      fg='white')
        email_label.pack(pady=10)
        
        my_mail = tk.StringVar()
        
        email = tk.Entry(self,
                                                              textvariable=my_mail,
                                                              font=('orbitron',12),
                                                              width=22)
        email.focus_set()
        email.pack(ipady=7)
        

        password_label = tk.Label(self,
                                                      text='Enter your password',
                                                      font=('orbitron',13),
                                                      bg='#3d3d5c',
                                                      fg='white')
        password_label.pack(pady=10)

        my_password = tk.StringVar()
       
        password_entry_box = tk.Entry(self,
                                                              textvariable=my_password,
                                                              font=('orbitron',12),
                                                              width=22)
        
        password_entry_box.pack(ipady=7)
# handle_focus_in() : remplacer le text par des etoiles
        def handle_focus_in(_):
            password_entry_box.configure(fg='black',show='*')
#bind permet de cachée le mot de passe 
        password_entry_box.bind('<FocusIn>',handle_focus_in)

# verificaiton de l'identité de l'utilisateur
        def check_password():
            #pour recuperer les valeures 
            m=my_mail.get()
            p= my_password.get()
            #import du base de donnée
            conn=DataBase.get_conn()
            conn.reconnect()
            cursor=conn.cursor()

            cursor.execute(('SELECT * FROM client WHERE email=%s AND password=%s ' ),(m, p))
            output = cursor.fetchall()
            for row in output:
                id=row[0]
                nom= row[1]
                prenom= row[2]
                mail = row[3]
                pssw = row[4]
           
            #Pour recupérer le client 
            cm = ClientDAO.findCompte(m)
            d = cm.get_client()
            
            if d.get_email()==m and d.get_password()==p:
                my_password.set('')
                incorrect_password_label['text']=''
                controller.show_frame('MenuPage')
            else:
               incorrect_password_label['text']='Incorrect Password'
                
        enter_button = tk.Button(self,
                                                     text='Enter',
                                                     command=check_password,
                                                     relief='raised',
                                                     borderwidth = 3,
                                                     width=40,
                                                     height=3)
        enter_button.pack(pady=10)
# Label des messages d'erreurs
        incorrect_password_label = tk.Label(self,
                                                                        text='',
                                                                        font=('orbitron',13),
                                                                        fg='white',
                                                                        bg='#33334d',
                                                                        anchor='n')
        incorrect_password_label.pack(fill='both',expand=True)

        