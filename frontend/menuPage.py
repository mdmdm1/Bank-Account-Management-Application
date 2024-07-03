import tkinter  as tk


# Page Menu

class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
   
        heading_label = tk.Label(self,
                                                     text='Admin',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                                           text='Main Menu',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#3d3d5c')
        main_menu_label.pack()
       

        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        bottom_frame = tk.Frame(self, width="40px", height="60px" ,borderwidth=3)
        bottom_frame.pack(fill='both',)

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

