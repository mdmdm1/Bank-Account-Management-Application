from backend.ConnectionDataBase import DataBase
import backend.Comptes
from datetime import datetime
class Operation :
    
    def __init__(self,types,montant,compte,date=datetime.now()):
        self.__date    = date
        self.__types   = types
        self.__montant = montant
        self.__compte  = compte
        self.__compte.ajouter(self)        

    def creer(self):
        conn=DataBase.get_conn()
        conn.reconnect()
        cursor=conn.cursor()
        reqO=('INSERT INTO operation VALUES(%s,%s,%s,%s,%s)')
        infosO=(cursor.lastrowid,self.__date,self.__types,self.__montant,self.__compte.get_id())
        cursor.execute(reqO,infosO)
        conn.commit()
        cursor.close()
        conn.close()
      
    def versement(self):
        conn=DataBase.get_conn()
        cursor=conn.cursor()
        self.__compte.set_solde(self.__compte.get_solde()+ self.__montant)
        don=('UPDATE comptes set soldes = soldes + %s WHERE id = %s')
        valeur=(self.__montant,self.__compte.get_id(),) 
        cursor.execute(don,valeur)
        cursor.close()
        conn.commit()
        self.creer()
        
    def retrait(self):
        if (self.__compte.get_solde() < self.__montant):
            print(" Impossible d'effectuer l'opération. Solde insuffisant !")
            quit()
        else:
            conn=DataBase.get_conn()
            cursor=conn.cursor()
            self.__compte.set_solde(self.__compte.get_solde()- self.__montant)
            don=('UPDATE comptes set soldes = soldes - %s WHERE id = %s')
            valeur=(self.__montant,self.__compte.get_id(),) 
            cursor.execute(don,valeur)
            conn.commit()
            cursor.close()
            conn.close()
            self.creer()
# Méthode qui nous permet de faire un virement   
    def virement(self,compte1=None):                    
        if(compte1 != None):
            if (self.__compte.get_solde() < self.__montant):
                print(" Impossible d'effectuer l'opération. Solde insuffisant !")
                quit()

            else:
                conn=DataBase.get_conn()
                cursor=conn.cursor()
                self.__compte.set_solde(self.__compte.get_solde()- self.__montant)
                don=('UPDATE comptes set soldes = soldes - %s WHERE id = %s')
                valeur=(self.__montant,self.__compte.get_id(),) 
                cursor.execute(don,valeur)
                conn.commit()     
                compte1.set_solde(compte1.get_solde()+ self.__montant)
                don=('UPDATE comptes set soldes = soldes + %s WHERE id = %s')
                valeur=(self.__montant,compte1.get_id(),) 
                cursor.execute(don,valeur)
                conn.commit()
                cursor.close()
                conn.close()
                self.creer()
                return self
                  
        
                   
      
        
        

      
                            
