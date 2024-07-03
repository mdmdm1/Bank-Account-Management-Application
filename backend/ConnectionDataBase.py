import mysql.connector
# Class de connection au base de données
class DataBase:
    __conn=None
    @staticmethod
    def get_conn():
        if DataBase.__conn is None:
            DataBase.__conn= mysql.connector.connect(host='localhost',database='banque',user='root', password='')
        return DataBase.__conn    


    
    
