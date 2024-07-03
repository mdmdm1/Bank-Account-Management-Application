from backend.ConnectionDataBase import DataBase
from backend.Comptes import Comptes
from backend.Client import Client
conn= DataBase.get_conn()
conn.reconnect()
################### Fonction Search ###################################""
class Search:
    def search(self,id):
        cursor=conn.cursor()
        Compteinfo=('SELECT * FROM comptes WHERE id=%s')
        info=(id,)
        cursor.execute(Compteinfo,info)
        resultat=cursor.fetchone()
        if resultat:
            Clientinfo=('SELECT * FROM client WHERE id=%s')
            info=(resultat[3],)
            cursor.execute(Clientinfo,info)
            resultat1=cursor.fetchone()
            cli=Client(resultat1[1],resultat1[2],resultat1[3],resultat1[4])
            c=Comptes(cli)
            return cli , c
            
        else:
            return None ,None
        

