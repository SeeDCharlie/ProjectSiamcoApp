import wx
from controls.controlDB import motorDB

class logginView(wx.Dialog):

    def __init__(self, parent, sizeView, urlIco):
        super(logginView, self).__init__(parent, title = "Loggin", size = sizeView)
        self.SetBackgroundColour("#DDDFDD")
        self.urlIco = urlIco + "/icons"
        #variables
        self.motor = motorDB(urlIco)
        self.x, self.y = self.Size
        
        #iconos
        self.iconUno = wx.StaticBitmap(self, -1, wx.Bitmap(wx.Image(self.urlIco + "/person.png", wx.BITMAP_TYPE_PNG)) )
        self.iconDos = wx.StaticBitmap(self, -1, wx.Bitmap(wx.Image(self.urlIco + "/user.png", wx.BITMAP_TYPE_PNG)) )
        self.iconTres = wx.StaticBitmap(self, -1, wx.Bitmap(wx.Image(self.urlIco + "/passw.png", wx.BITMAP_TYPE_PNG)) )
        
        #panel

        #sizers
        self.sizerUno = wx.BoxSizer(wx.VERTICAL)
        self.sizerDos = wx.BoxSizer( wx.HORIZONTAL)
        self.sizerTres = wx.BoxSizer( wx.HORIZONTAL)
        self.sizerCuatro = wx.BoxSizer( wx.HORIZONTAL)

        #textCtrl
        self.textCtrlUno = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER)
        self.textCtrlDos = wx.TextCtrl(self, style = wx.TE_PASSWORD | wx.TE_PROCESS_ENTER )

        #labels

        #buttons
        self.botonUno = wx.Button(self, -1, "Entrar")
        self.botonDos = wx.Button(self, -1, "Cancelar")

        #organizing sizers
        self.sizerDos.Add(self.iconDos, 2.5, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL,1)
        self.sizerDos.Add(self.textCtrlUno, 3, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT | wx.RIGHT, self.x*0.1)
        self.sizerTres.Add(self.iconTres, 2.5, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 1)
        self.sizerTres.Add(self.textCtrlDos, 3, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT | wx.RIGHT, self.x*0.1)
        self.sizerCuatro.Add(self.botonUno, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT | wx.RIGHT, self.x*0.1)
        self.sizerCuatro.Add(self.botonDos, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT | wx.RIGHT | wx.LEFT, self.x*0.1)


        self.sizerUno.Add(self.iconUno, 1, wx.CENTER | wx.ALL, 5)
        self.sizerUno.Add(self.sizerDos, 1, wx.EXPAND | wx.ALL, 5)
        self.sizerUno.Add(self.sizerTres, 1, wx.EXPAND | wx.ALL, 5)
        self.sizerUno.Add(self.sizerCuatro, 1, wx.EXPAND | wx.ALL, 5)
        #events
        self.Bind(wx.EVT_BUTTON, self.logginAction, self.botonUno )
        self.Bind(wx.EVT_BUTTON, self.exitAction, self.botonDos )
        self.Bind(wx.EVT_TEXT_ENTER, self.logginAction, self.textCtrlUno)
        self.Bind(wx.EVT_TEXT_ENTER, self.logginAction, self.textCtrlDos)
        self.Bind( wx.EVT_CLOSE, self.ParentFrameOnClose )

        self.SetSizer(self.sizerUno)
        self.Layout()
        self.Center()
        
    def ParentFrameOnClose(self, event):
        self.motor.closeDB()
        self.DestroyChildren()
        self.Destroy()

    def logginAction(self, evt):
        username = self.textCtrlUno.GetValue()
        passw = self.textCtrlDos.GetValue()

        result = self.motor.execEstatements("select name from users where userName = ? and pass = ?", (username, passw,)).fetchone()
        print("resultado id user : ", result)

        if result != None:
            self.motor.closeDB()
            wx.MessageDialog(None, "Bienvenido %s"%result , "SiamcoApp", wx.OK).ShowModal()
            self.EndModal(True)
        elif username != "" and passw != "" :
            wx.MessageDialog(None, "Usuario o contraseña incorrectos" , "SiamcoApp", wx.OK).ShowModal()

    def exitAction(self, evt):
        self.motor.closeDB()
        self.loggin = True
        self.EndModal(False)
