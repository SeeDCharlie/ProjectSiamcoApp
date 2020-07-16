import sqlite3
from sqlite3 import Error
import os
import requests
from unidecode import unidecode

class motorDB():

    def __init__(self, url):
        self.conexion = None
        self.db_url = fr"{url}/db/siamco_db.db"
        self.cursor = None

        if not self.existsDB():
            print("creando db")
            self.createDB()
            print("db creada!")
        else :
            self.checkUpdates()

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
        print("Conexion cerrada!!")
        self.conexion.close()
    
    def execEstatement(self, statement):
        return self.cursor.execute(statement)
    
    def execEstatements(self, statement, dats):
        return self.cursor.execute(statement, dats)

    def existsDB(self):
        return os.path.exists(self.db_url)

    def createDB(self):
        self.createConexion()
        url = "https://raw.githubusercontent.com/SeeDCharlie/ProjectSiamcoApp/master/dbSqlite/dbSiamco.db.sql"
        r = requests.get(url, allow_redirects=True).text
        self.conexion.executescript(r)
        self.conexion.commit()

    def checkUpdates(self):
        url = "https://raw.githubusercontent.com/SeeDCharlie/ProjectSiamcoApp/master/updateApp.seed"
        r = requests.get(url, allow_redirects=True).text
        r = r.strip()
        print("valor 'r' : ", r)
        if r == "True":
            print("Actualizando!!...")
            os.remove(self.db_url)
            if not self.existsDB():
                print("Actualizado!!!")
                self.createDB()
                return True
            else:
                print("nos se pudo actualizar la base de datos!!")
                self.createConexion()
                return False
        else:
            self.createConexion()
            return True
"""
motor = motorDB("/home/seed/Documentos/siamco_db/app/")
listaAct = motor.execEstatement("select cod, description, und, value from activities;").fetchall()
for act in enumerate(listaAct):
    print(act)

motor.closeDB()
"""



