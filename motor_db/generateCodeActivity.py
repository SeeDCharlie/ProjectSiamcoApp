import codecs
from unidecode import unidecode
import os
import pandas as pd

class manageFile():

    def generateCodes(self, url):
        
        fileActivitys = open(url+"demo_activities_official.csv", encoding="UTF-8")
        newFileActivitys = open (url+"SIAMCO_ACTIVITIES.csv","w", encoding="UTF-8")
        for cod, line in enumerate(fileActivitys.readlines()):
            try:
                if line[0] != " " or line[0] != '\n' or line[0] != "/" or line != "":
                    #print("linea : ", line)
                    dats = line.split("|")
                    #print("dats [] : ", dats)
                    registro = "1|%s|%s|%s|%s|1|||1|1\n"%("S"+str(cod + 1).rjust(3,"0"), dats[0], dats[1], dats[2][:-1] )
                    newFileActivitys.write(registro)
                    #print("registro creado %d: %s"%(cod, registro))
            except:
                print("error el dato esta erroneo : ", dats)
        fileActivitys.close()
        newFileActivitys.close()

    def clearDomoFile(self, url):
        fileActivitys = open(url+"demo_activities1.csv", "r", encoding="UTF-8")
        newFileActivitys = open (url+"demo_activities_official.csv","w")

        for line in fileActivitys.readlines():
            if line.find("/") == -1 and line[0] != "\n" and line[0] != " ":
                line = line.replace(":", " ")
                line = line.replace("(", " ")
                line = line.replace(")", " ")
                line = line.replace("'", "")
                line = line.replace(",", ".")
                line = line.replace("=", "igual a")
                line = line.replace("*", "x")
                newFileActivitys.write(line)
        #29433808
        fileActivitys.close()
        newFileActivitys.close()

    def generateFileReport(self, url):
        fileActivitys = open(url, "r", encoding="utf-8")
        newFileActivitys = open ("actividades_a_revisar.txt","w")
        uni = {'94':'Unidad' , 'LM': 'Metro Lineal', 'MTK': 'Metro Cuadrado', 'MTQ': 'Metro Cubico','MTR': 'Metro',
                'MTQ': 'Metros Cubicos'}
        for line in fileActivitys.readlines():
            if line[0] == " " or line[0] == "\n" or line[0] == "/":
                newFileActivitys.write(line)
            else:
                try:
                    dats = line.split("|")
                except :
                    print("linea erronea : ", line)
                else:
                    wLine = "Actividad: %s  Unidad de medida : %s    Valor unitario: %s"%(dats[0].ljust(110, "."), uni[dats[1].strip()].ljust(16, " "), dats[2] )
                    newFileActivitys.write(wLine)

        fileActivitys.close()
        newFileActivitys.close()

    def review_to_demo(self, url):
        fileActivitys = open(url+"activities_review.txt", "r", encoding="UTF-8")
        newFileActivitys = open (url+"demo_activities1.csv","w")
        uni = {'Unidad':'94' , 'Metro Lineal': 'LM', 'Metro Cuadrado': 'MTK', 'Metros Cubicos': 'MTQ','Metro Cubico': 'MTQ', 'Metro': 'MTR'}
        for line in fileActivitys.readlines():
            if line.find("/") == -1 and line[0] != "\n" and line[0] != " ":
                line = line.replace(".", "")
                dats = line.split(":")
                print("linea a insertar : " , dats)
                dats[2] = dats[2].strip().split("  ")[0].strip()
                dats[3] = dats[3].strip()
                if dats[1].find("  ") > 0 :
                    dats[1] = dats[1].split("  ")[0]
                dats[1] = dats[1].strip()
                newFileActivitys.write("%s|%s|%s\n"%(dats[1], uni[dats[2]], dats[3] ) )
        fileActivitys.close()
        newFileActivitys.close()

    def generateFileDB(self):
        ruta = "/home/seed/Documentos/siamco_db/filesCsv/"
        newFile =  open(ruta + "activitys_db.csv", "w")
        fActivitys = open(ruta + "SIAMCO_ACTIVITIES.csv", "r", encoding="UTF-8")

        uni = {'94':'Unidad' , 'LM': 'Metro Lineal', 'MTK': 'Metro Cuadrado', 'MTQ': 'Metro Cubico','MTR': 'Metro',
                'MTQ': 'Metros Cubicos', 'WM': 'Mes de trabajo'}
        product = { '1':'Servicio', '2' : 'Producto'}
        iva = {'1': 'IVA: Exento 0%', '2': 'IVA: Tarifa General 16%', '4' : 'IVA: Tarifa Diferencial 5%', '5' : 'IVA: Excluido 0%', '6' : 'IVA: Tarifa General 19%', '0':'IVA: No Tiene'}
        inc = {'2': 'INC: 2%','4': 'INC: 4%','8': 'INC: 8%', '16':'INC: 16%', '0':'INC: No Tiene'}
    
        newFile.write("tipo_producto,Codigo,Descripcion,unidad_medida,Valor_unitario,IVA,IC,INC,Cantidad_real,Cantidad_paquete\n")

        for line in fActivitys.readlines():
            dats = line.split("|")
            dats = self.convertVoidToCero(dats)
            print("datos : ", dats)
            newLine = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%(product[dats[0]], dats[1], dats[2], uni[dats[3]], dats[4], iva[dats[5]], dats[6], inc[dats[7]], dats[8], dats[9] )
            newFile.write(newLine)

        newFile.close()
        fActivitys.close()

        self.converCsvToExcel(ruta)
    
    def converCsvToExcel(self, ruta):
        csv = pd.read_csv(ruta+'activitys_db.csv', error_bad_lines=False)
        csv.to_excel(ruta + 'actvitys_db.xlsx', index = None, header=True)
        print("Ok!")

    def convertVoidToCero(self,lista):
        newlist = []
        for i in range(len(lista)):
            newlist.append(lista[i])
            if lista[i] == '':
                newlist[i]= '0'

        return newlist

manage = manageFile()
manage.generateFileDB()

"""manage.review_to_demo("/home/seed/Documentos/siamco_db/filesCsv/")
manage.clearDomoFile("/home/seed/Documentos/siamco_db/filesCsv/")
manage.generateCodes("/home/seed/Documentos/siamco_db/filesCsv/")"""