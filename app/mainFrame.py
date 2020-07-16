import wx
import os
from controls.controlDB import motorDB 
from views.frameLoggin import logginView
from views.frameGenerateCot import generateCotView


class mainView(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title=("Siamco_App"), size=wx.GetDisplaySize())
        
        self.SetBackgroundColour(wx.WHITE)

        #variables
        self.urldir = os.path.dirname(__file__)
        self.controlDB = motorDB(self.urldir)
        self.logginAction(self.urldir)

        #sizers
        sizerUno = wx.BoxSizer(wx.VERTICAL)
        
        #notebooks

        self.notebookUno = wx.Notebook(self)
        self.pageOne = self.notebookUno.AddPage(generateCotView(self.notebookUno), "Generar Cotizacion")
        self.loadImageBook()
        #organizing sizers
        sizerUno.Add(self.notebookUno, 1, wx.EXPAND | wx.ALL, 1)

        #events
        self.Bind( wx.EVT_CLOSE, self.ParentFrameOnClose )


        self.SetSizer(sizerUno)
        self.Layout()
        self.Centre()
    
    def ParentFrameOnClose(self, event):
        self.controlDB.closeDB()
        print("cerrando !!")
        self.DestroyChildren()
        self.Destroy()

    def logginAction(self, urldir):
        loggin = logginView(self, (self.Size[0]/2, self.Size[1]/2 ), urldir).ShowModal()
        if loggin == 5101 or loggin == 0:
            self.ParentFrameOnClose(wx.EVT_CLOSE)
    
    def loadImageBook(self):
        li = wx.ImageList(32 , 32)
        rl = []
        
        for i, f in enumerate(os.listdir(self.urldir+"/icons/iconsNoteBmainFrame" )):
            print("ruta imagen : ", self.urldir+"/icons/iconsNoteBmainFrame/%s"%f )
            rl.append(li.Add(wx.Bitmap(self.urldir+"/icons/iconsNoteBmainFrame/%s"%f , wx.BITMAP_TYPE_PNG )))
        self.notebookUno.AssignImageList(li)
        for  imag in rl:
            self.notebookUno.SetPageImage(i, imag)

    


if __name__ == "__main__":
    app = wx.App()
    v = mainView()
    v.Show()
    app.MainLoop()