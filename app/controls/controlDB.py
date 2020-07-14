import sqlite3
from sqlite3 import Error
import os

class motorDB():

    def __init__(self):
        self.conexion = None
        self.db_url = fr"{os.path.abspath(os.getcwd())}/app/db/siamco_db.db"
        self.cursor = None

        self.createConexion()

        if not self.existsDB():

            
                
    def createConexion(self):
        try:
            self.conexion = sqlite3.connect(self.db_url)
            print(sqlite3.version)

        except Error as e:
            print(e)
        finally:
            if self.conexion:
                self.cursor = self.conexion.cursor()
                print("conexion exitosa!")
    
    def closeDB(self):
        self.conexion.close()
    
    def execEstatement(self, statement):
        self.cursor.execute(statement)
                
    def existsDB(self):
        return os.path.exists(self.db_url)

    def createDB(self):
        
