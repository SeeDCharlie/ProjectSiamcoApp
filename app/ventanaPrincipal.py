import wx
from controls.controlDB import motorDB 


class mainView(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title=("Siamco_App"), size=wx.GetDisplaySize())
        self.SetBackgroundColour(wx.WHITE)

        #variables
        self.controlDB = motorDB()

        self.Layout()
        self.Centre()

if __name__ == "__main__":
    app = wx.App()
    v = mainView()
    v.Show()
    app.MainLoop()