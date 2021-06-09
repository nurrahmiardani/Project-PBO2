import wx 
import desain

class Kain(desain.MyFrame1):
    def __init__(self, parent):
        super().__init__(parent)

app = wx.App()
tampilan = Kain(parent=None).Show()
app.MainLoop()