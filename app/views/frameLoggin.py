import wx

class logginView(wx.Dialog):

    def __init__(self, parent, sizeView, urlIco):
        super(logginView, self).__init__(parent, title = "Loggin", size = sizeView)
        self.SetBackgroundColour(wx.WHITE)

        #variables

        #iconos
        self.iconUno = wx.StaticBitmap(self, -1, wx.BitmapFromImage(wx.Image(urlIco + "/person.png", wx.BITMAP_TYPE_PNG))) 
        self.iconDos = wx.StaticBitmap(self, -1, wx.BitmapFromImage(wx.Image(urlIco + "/user.png", wx.BITMAP_TYPE_PNG)))
        self.iconTres = wx.StaticBitmap(self, -1, wx.BitmapFromImage(wx.Image(urlIco + "/passw.png", wx.BITMAP_TYPE_PNG)))
        
        #panel

        #sizers
        self.sizerUno = wx.BoxSizer(wx.VERTICAL)
        self.grid_uno = wx.FlexGridSizer( 3, 2, 1 , self.Size[1]*0.30)

        #textCtrl
        self.textCtrlUno = wx.TextCtrl(self)
        self.textCtrlDos = wx.TextCtrl(self)

        #labels
        #self.labelUno = wx.StaticText(self, -1, "Usuario")
        #self.labelDos = wx.StaticText(self, -1, "Contraseña")

        #buttons
        self.botonUno = wx.Button(self, -1, "Entrar")
        self.botonDos = wx.Button(self, -1, "Salir")

        #organizing sizers
        self.grid_uno.AddMany([(self.iconDos, 2 , wx.CENTER | wx.EXPAND | wx.LEFT, self.Size[0]*0.40),
                            (self.textCtrlUno, 100, wx.CENTER | wx.EXPAND | wx.ALL, 5),
                            (self.iconTres, 2 , wx.EXPAND | wx.LEFT, self.Size[0]*0.40),
                            (self.textCtrlDos, 3 , wx.EXPAND | wx.ALL, 5),
                            (self.botonUno, 1 , wx.EXPAND | wx.ALL, 5),
                            (self.botonDos, 1 , wx.EXPAND | wx.ALL, 5)])
        self.grid_uno.AddGrowableRow(1, 1)
        self.grid_uno.AddGrowableCol(1, 1)

        self.sizerUno.Add(self.iconUno, 1, wx.CENTER | wx.ALL, 5)
        self.sizerUno.Add(self.grid_uno, 1, wx.EXPAND | wx.ALL, 5)
        #events
        self.Bind(wx.EVT_BUTTON, self.logginAction, self.botonUno )
        self.Bind(wx.EVT_BUTTON, self.exitAction, self.botonDos )
        self.SetSizer(self.sizerUno)
        self.Layout()
        self.Center()

    def logginAction(self, evt):
        print("")
        self.EndModal(True)

    def exitAction(self, evt):
        self.loggin = True
        self.EndModal(False)