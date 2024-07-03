import backend.Client
import sys
import backend.Comptes
from backend.ConnectionDataBase import DataBase
from backend.Client import Client
from backend.Comptes import Comptes

class ClientDAO:
    def __init__(self) -> None:
        pass
    #pour chercher le client avec l'id client
    def findClient(id_c):
        #c1 = Client
        from backend.ConnectionDataBase import DataBase
        conn=DataBase.get_conn()
        conn.reconnect()
            
        cursor=conn.cursor()

        cursor.execute(('SELECT * FROM client WHERE id=%s' ),(id_c, ))
        output = cursor.fetchall()
        nom=None
        prenom=None
        mail=None
        pssw=None
        for row in output:
                nom= row[1]
                prenom= row[2]
                mail = row[3]
                pssw = row[4]
        c1 = Client(nom, prenom, mail, pssw)
        return c1
    #pour chercher le compte avec l'email
    def findCompte(email): 
        C = Comptes
        c1 = Client
        global id_c 
        id_c= 0
        
        conn= DataBase.get_conn()
        conn.reconnect()
            
        cursor=conn.cursor()
        
        cursor.execute(('SELECT * FROM client WHERE email=%s' ),(email,))
        output = cursor.fetchall()
        id_t=0
        for row in output:
                id_t= row[0]
                solde= row[1]
                date = row[2]
        
        id_c = id_t
        cursor.execute(('SELECT * FROM comptes WHERE idClient=%s' ),(id_c,))
        output = cursor.fetchall()
        solde=0
        for row in output:
                id= row[0]
                solde= row[1]
                date = row[2]
        c= ClientDAO.findClient(id_c)
        compte = Comptes(c, solde)
        return compte
    #pour chercher le compte avec l'id client
    def findCompte2(id_c): 
        C = Comptes
        c1 = Client
        conn=DataBase.get_conn()
        conn.reconnect()
            
        cursor=conn.cursor()
        
        
        cursor.execute(('SELECT * FROM comptes WHERE idClient=%s' ),(id_c,))
        output = cursor.fetchall()
        solde =0
        for row in output:
                id= row[0]
                solde= row[1]
                date = row[2]
        c= ClientDAO.findClient(id_c)
        compte = Comptes(c, solde)
        return compte

#pour chercher le compte avec l'id compte
    def findCompte3(id_c): 
        C = Comptes
        c1 = Client
        conn=DataBase.get_conn()
        conn.reconnect()
            
        cursor=conn.cursor()
        
        
        cursor.execute(('SELECT * FROM comptes WHERE id=%s' ),(id_c,))
        output = cursor.fetchall()
        solde =0
        for row in output:
                id= row[0]
                solde= row[1]
                date = row[2]
                id_cl= row[3]
        c= ClientDAO.findClient(id_cl)
        compte = Comptes(c, solde)
        return compte
