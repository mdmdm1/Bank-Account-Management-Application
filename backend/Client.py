
from backend.ConnectionDataBase import DataBase
# pour creer un client
class Client :
    
    def __init__(self,nom,prenom,mail,password):
        self.__nom= nom
        self.__prenom= prenom
        self.__email= mail
        self.__password=password
        self.__Comptes = []
        conn=DataBase.get_conn()
        conn.reconnect()
        cursor=conn.cursor()
        donnee=('SELECT * FROM client WHERE email=%s')
        info=(self.__email,)
        cursor.execute(donnee,info)
        resultat=cursor.fetchone()
        if not resultat:
            cursor.execute(('INSERT INTO client VALUES(%s,%s,%s,%s,%s)'),(cursor.lastrowid,self.__nom,self.__prenom,self.__email,self.__password))
            conn.commit()
            self.__num=cursor.lastrowid
        else:
            self.__num=resultat[0]
        
    def get_num(self):
        return self.__num
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password
       

    def modifierinfo(self,nom,prenom,email,password):
        self.__nom= nom
        self.__prenom= prenom
        self.__email= email
        self.__password= password
   
    def affiche(self):
         print(self.__nom ,self.__prenom,self.__email)
    
    def ajouter(self,compte):
         self.__Comptes.append(compte)  
         
    
    
