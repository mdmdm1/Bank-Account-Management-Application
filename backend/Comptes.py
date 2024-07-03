from backend.ConnectionDataBase import DataBase
import backend.Operation
import backend.Client
from datetime import datetime

# pour creer un compte
class Comptes:
    def __init__(self,client,solde=0.0):
        self.__operations = []
        self.__client     = client
        self.__client.ajouter(self)
        self.__dates=datetime.now()
        
        conn=DataBase.get_conn()
        conn.reconnect()
        cursor=conn.cursor()
        cursor.execute(('SELECT * FROM comptes WHERE idClient=%s'),(self.__client.get_num(),))
        resultat=cursor.fetchone()
        if not resultat:
            self.__solde      = solde
            cursor.execute(('INSERT INTO comptes VALUES(%s,%s,%s,%s)'),(cursor.lastrowid,self.__solde,self.__dates,self.__client.get_num()))
            conn.commit()
            self.__id=cursor.lastrowid
        else:
            self.__id=resultat[0]
            self.__solde      = resultat[1]
            
        
        
        
         

    def get_id(self):
        return self.__id     
    def client(self):
        pass
    def AfficheSolde(self):
        pass
    def afficherOperation(self):
        pass
    
    def ajouter(self,operation):
        pass
    def set_solde(self,solde):
        self.__solde = solde
    def get_solde(self):
        return self.__solde  
    def affiche(self):
         print(self.__solde)

    def get_client(self):
        return self.__client