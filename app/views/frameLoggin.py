import wx

class logginView(wx.Dialog):

    def __init__(self, parent, sizeView):
        super(logginView, self).__init__(parent, title = "Loggin", size = sizeView)
        self.SetBackgroundColour(wx.WHITE)

        #variables
        self.loggin = False

        #panel
        self.panel = wx.Panel(self) 

        #sizers
        self.grid_uno = wx.GridSizer( 3, 2, 1 , 1)

        #textCtrl
        self.textCtrlUno = wx.TextCtrl(self)
        self.textCtrlDos = wx.TextCtrl(self)

        #labels
        self.labelUno = wx.StaticText(self, -1, "Usuario")
        self.labelDos = wx.StaticText(self, -1, "Contraseña")

        #buttons
        self.botonUno = wx.Button(self, -1, "Entrar")
        self.botonDos = wx.Button(self, -1, "Salir")

        #organizing sizers
        self.grid_uno.Add(self.labelUno, 1 , wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.grid_uno.Add(self.textCtrlUno, 1 , wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.grid_uno.Add(self.labelDos, 1 , wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5 )
        self.grid_uno.Add(self.textCtrlDos, 1 , wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.grid_uno.Add(self.botonUno, 1 , wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.grid_uno.Add(self.botonDos, 1 , wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        #events
        self.Bind(wx.EVT_BUTTON, self.logginAction, self.botonUno )
        self.Bind(wx.EVT_BUTTON, self.exitAction, self.botonDos )
        self.SetSizer(self.grid_uno)
        self.Layout()
        self.Center()

    def logginAction(self, evt):
        print("")
        self.EndModal(True)

    def exitAction(self, evt):
        self.loggin = True
        self.EndModal(False)