import wx
import wx.grid as grid
from controls.controlDB import motorDB

class generateCotView(wx.Panel):
    

    def __init__(self, parent, motor, urldir):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour("white")
        #variables
        self.motor = motor
        self.urldir = "%s/icons/iconsGenerateCot"%urldir
        #panels

        #sizers
        sizerUno = wx.BoxSizer(wx.HORIZONTAL)

        sizerDos = wx.BoxSizer(wx.VERTICAL)
        sizerTres = wx.BoxSizer(wx.HORIZONTAL)

        sizerCuatro = wx.BoxSizer(wx.VERTICAL)
        sizerCinco = wx.BoxSizer(wx.HORIZONTAL)
        sizerSeis = wx.BoxSizer(wx.HORIZONTAL)
        sizerSiete = wx.BoxSizer(wx.HORIZONTAL)
        sizerOcho = wx.BoxSizer(wx.HORIZONTAL)
        sizerNueve = wx.BoxSizer(wx.HORIZONTAL)
        sizerDiez = wx.BoxSizer(wx.HORIZONTAL)

        #icons
        self.iconUno = wx.StaticBitmap(self, -1, wx.Bitmap(wx.Image("%s/buscar.png"%self.urldir, wx.BITMAP_TYPE_ANY)) )

        #buttons
        picUno = wx.Bitmap("%s/mas.png"%self.urldir, wx.BITMAP_TYPE_ANY)
        self.buttonUno = wx.BitmapButton(self,-1, picUno, style=wx.BORDER_NONE)
        picDos = wx.Bitmap("%s/cerrar.png"%self.urldir, wx.BITMAP_TYPE_ANY)
        self.buttonDos = wx.BitmapButton(self,-1, picDos, style=wx.BORDER_NONE)
        picTres = wx.Bitmap("%s/crear.png"%self.urldir, wx.BITMAP_TYPE_ANY)
        self.buttonTres = wx.BitmapButton(self,-1, picTres, style=wx.BORDER_NONE)

        #labels
        self.labelUno = wx.StaticText(self, -1, "Buscar")
        self.labelDos = wx.StaticText(self, -1, "Cliente")
        self.labelTres = wx.StaticText(self, -1, "Nombre del Proyecto")
        self.labelCuatro = wx.StaticText(self, -1, "Autor")
        self.labelCinco = wx.StaticText(self, -1, "Numero de Propuesta")
        self.labelSeis = wx.StaticText(self, -1, "Email")
        self.labelSiete = wx.StaticText(self, -1, "Duracion de la obra")
        self.labelOcho = wx.StaticText(self, -1, "Cotizacion")
        self.labelNueve= wx.StaticText(self, -1, "Sub Total Costo Directo(MO + Materiales)")
        self.labelDiez = wx.StaticText(self, -1, "Gastos Administrativos (11%)")
        self.labelOnce = wx.StaticText(self, -1, "Imprevistos (4%)")
        self.labelDoce = wx.StaticText(self, -1, "Utilidad (5%)")
        self.labelTrece = wx.StaticText(self, -1, "Iva sobre utilidad (19%)")
        self.labelCatorce = wx.StaticText(self, -1, "Costo Total Directo + Costo Total Indirecto")

        #lines
        self.line_uno = wx.StaticLine(self, -1, size =(400, 1), style = (wx.LI_VERTICAL ))
        self.line_dos = wx.StaticLine(self, -1, size = (400, 1), style = (wx.LI_VERTICAL) )
        self.lineDuno = wx.StaticLine(self, -1, size = (400, 1), style = (wx.LI_VERTICAL) )
        self.line_tres = wx.StaticLine(self, -1, style = (wx.LI_HORIZONTAL) )

        #tables

        self.tablaUno = grid.Grid(self, -1)
        self.tablaDos = grid.Grid(self, -1, size=(600,200))
        self.tablaUno.SetRowLabelSize(0)
        self.tablaDos.SetRowLabelSize(0)
        self.createTableActivities()
        self.tablaUno.SetMargins(0,0)
        self.tablaDos.SetMargins(0,0)


        #textCtrl

        self.textCtrlBuscar = wx.TextCtrl(self)
        self.textCtrlUno = wx.TextCtrl(self)
        self.textCtrlDos = wx.TextCtrl(self)
        self.textCtrlTres = wx.TextCtrl(self)
        self.textCtrlCuatro = wx.TextCtrl(self)
        self.textCtrlCinco = wx.TextCtrl(self)
        self.textCtrlSeis = wx.TextCtrl(self)

        #organizing sizers
        sizerTres.Add(self.iconUno, 1, wx.CENTRE | wx.ALL, 1 )
        sizerTres.Add(self.labelUno, 1, wx.CENTER | wx.ALL, 1 )
        sizerTres.Add(self.textCtrlBuscar, wx.ALIGN_LEFT | 1, wx.CENTRE | wx.ALL, 1)
        sizerTres.AddSpacer(100)
        sizerTres.Add(self.buttonUno, 1, wx.CENTRE | wx.ALL, 1 )
        sizerTres.Add(self.buttonDos, 1, wx.CENTRE | wx.ALL, 1 )
        sizerTres.Add(self.buttonTres, 1, wx.CENTRE | wx.ALL, 1 )

        sizerDos.Add(sizerTres, 1, wx.EXPAND | wx.ALL, 1)
        sizerDos.Add(self.line_uno, 0, wx.EXPAND | wx.ALL, 6)
        sizerDos.Add(self.tablaUno, 1,  wx.CENTER | wx.ALL , 1)
        sizerDos.AddSpacer(20)

        sizerCinco.Add(self.labelDos, 1, wx.ALIGN_LEFT | wx.ALL, 1)
        sizerCinco.Add(self.textCtrlUno, 1, wx.ALIGN_LEFT | wx.ALL, 1)

        sizerSeis.Add(self.labelTres, 1, wx.ALIGN_LEFT | wx.ALL, 1)
        sizerSeis.Add(self.textCtrlDos, 1, wx.ALIGN_LEFT | wx.ALL, 1)

        sizerSiete.Add(self.labelCuatro, 1, wx.ALIGN_LEFT | wx.ALL, 1)
        sizerSiete.Add(self.textCtrlTres, 1, wx.ALIGN_LEFT | wx.ALL, 1)

        sizerOcho.Add(self.labelCinco, 1, wx.ALIGN_LEFT | wx.ALL, 1)
        sizerOcho.Add(self.textCtrlCuatro, 1, wx.ALIGN_LEFT | wx.ALL, 1)

        sizerNueve.Add(self.labelSeis, 1, wx.ALIGN_LEFT | wx.ALL, 1)
        sizerNueve.Add(self.textCtrlCinco, 1, wx.ALIGN_LEFT | wx.ALL, 1)

        sizerDiez.Add(self.labelSiete, 1, wx.ALIGN_LEFT | wx.ALL, 1)
        sizerDiez.Add(self.textCtrlSeis, 1, wx.ALIGN_LEFT | wx.ALL, 1)

        sizerCuatro.Add(self.labelOcho, 1, wx.ALIGN_LEFT | wx.ALL, 1)
        sizerCuatro.Add(self.tablaDos, 1, wx.CENTER | wx.ALL, 1 )
        sizerCuatro.Add(self.line_dos, 0, wx.EXPAND | wx.ALL, 5 )
        sizerCuatro.Add(sizerCinco, 1, wx.EXPAND | wx.ALL, 1)
        sizerCuatro.Add(sizerSeis, 1, wx.EXPAND | wx.ALL, 1)
        sizerCuatro.Add(sizerSiete, 1, wx.EXPAND | wx.ALL, 1)
        sizerCuatro.Add(sizerOcho, 1, wx.EXPAND | wx.ALL, 1)
        sizerCuatro.Add(sizerNueve, 1, wx.EXPAND | wx.ALL, 1)
        sizerCuatro.Add(sizerDiez, 1, wx.EXPAND | wx.ALL, 1)
        sizerCuatro.Add(self.lineDuno, 0, wx.EXPAND | wx.ALL, 5 )
        sizerCuatro.Add(self.labelNueve, 1, wx.EXPAND | wx.ALL, 1)
        sizerCuatro.Add(self.labelDiez, 1, wx.EXPAND | wx.ALL, 1)
        sizerCuatro.Add(self.labelOnce, 1, wx.EXPAND | wx.ALL, 1)
        sizerCuatro.Add(self.labelDoce, 1, wx.EXPAND | wx.ALL, 1)
        sizerCuatro.Add(self.labelTrece, 1, wx.EXPAND | wx.ALL, 1)
        sizerCuatro.Add(self.labelCatorce, 1, wx.EXPAND | wx.ALL, 1)
        sizerCuatro.AddSpacer(20)

        #------------------------------------------------- 
        sizerUno.Add(sizerDos, 1, wx.EXPAND | wx.ALL, 10)
        sizerUno.Add(self.line_tres, 0,  wx.EXPAND | wx.ALL, 5)
        sizerUno.Add(sizerCuatro, 1, wx.EXPAND | wx.ALL, 12)

        self.SetSizer(sizerUno)
    
    def createTableActivities(self):
        self.insertLabelColumnTable()
        listaAct = self.motor.execEstatement("select cod, description, und, value from activities;").fetchall()
        print("selection mode : ", self.tablaUno.GetSelectionMode())
        for i, act in enumerate(listaAct):
            self.tablaUno.AppendRows()
            for j, dat in enumerate(act):
                self.tablaUno.SetCellValue(i,j, str(dat))
        self.tablaUno.SetColSize(1, wx.GetDisplaySize()[0]*0.2)
        self.tablaDos.SetColSize(0, wx.GetDisplaySize()[0]*0.2)
        self.tablaUno.Scroll(0,0)
        self.tablaDos.Scroll(0,0)


    def insertLabelColumnTable(self):
        nColums = ["COD","Descripcion", "Uni Medida","Valor"]
        self.tablaUno.CreateGrid(0, 4, 1)
        for i, name in enumerate(nColums):
            self.tablaUno.SetColLabelValue(i, name)
        self.createLabelCulumnTableDos()
    def createLabelCulumnTableDos(self):
        self.tablaDos.CreateGrid(0, 5)
        nColums = ["Descripcion", "Uni Medida","Valor Uni","Cant","Valor Total"]
        for i, name in enumerate(nColums):
            self.tablaDos.SetColLabelValue(i, name)

