import wx
import gui

class CalcFrame(gui.MyFrame1):
    def __init__(self,parent):
        gui.MyFrame1.__init__(self,parent)

    def search_player(self,event):
        print("comming soon")

app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)

app.MainLoop()
