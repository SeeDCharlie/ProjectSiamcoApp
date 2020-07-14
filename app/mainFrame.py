import wx
from controls.controlDB import motorDB 
from views.frameLoggin import logginView

class mainView(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title=("Siamco_App"), size=wx.GetDisplaySize())
        self.SetBackgroundColour(wx.WHITE)

        #variables
        self.controlDB = motorDB()

        loggin = logginView(self, (self.Size[0]/2, self.Size[1]/2 )).ShowModal()
        print("return modal : ", loggin)

        self.Layout()
        self.Centre()

if __name__ == "__main__":
    app = wx.App()
    v = mainView()
    v.Show()
    app.MainLoop()