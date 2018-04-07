#coding=utf-8
import wx

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self,None,-1,"python菜单栏练习")
        self.panel = wx.Panel(self)
        #设置菜单栏与子菜单
        menubar = wx.MenuBar()
        menu1 = wx.Menu()
        menu3 = wx.Menu()
        bbu1 = menu1.Append(-1,"B2200")
        bbu2 = menu1.Append(-1,"B3200")
        cc1 = menu3.Append(-1,"cc1")
        cc2 = menu3.Append(-1, "cc2")
        cc3 = menu3.Append(-1, "cc3")
        menu1.AppendMenu(-1,"CC",menu3)
        self.Bind(wx.EVT_MENU,self.One_Play,bbu1)
        self.Bind(wx.EVT_MENU, self.One_Play, bbu2)
        menubar.Append(menu1,"BBU")
        menu2 = wx.Menu()
        menu2.AppendSeparator()
        rru1 = menu2.Append(-1,"R2254")
        rru2 = menu2.Append(-1,"R2252")
        self.Bind(wx.EVT_MENU, self.Two_Play, rru1)
        self.Bind(wx.EVT_MENU, self.Two_Play, rru2)
        menubar.Append(menu2,"RRU")
        #设置弹出菜单
        self.Menu4 = wx.Menu()
        self.Menu4.Append(-1,"1")
        self.Menu4.Append(-1, "2")
        self.Menu4.Append(-1, "3")
        self.Menu4.Append(-1, "4")
        self.Bind(wx.EVT_CONTEXT_MENU,self.Menu4_Test)
        self.SetMenuBar(menubar)
        print menubar.GetLabelTop(0)
        print menubar.FindMenu("BBU")
        #状态栏
        status = self.CreateStatusBar()
        status.SetStatusText("write bu zhouqiang")

    def One_Play(self,event):
        print "this is BBU"

    def Two_Play(self,event):
        print "this is RRU"

    def Menu4_Test(self,event):
        pos = event.GetPosition()
        print pos
        pos = self.panel.ScreenToClient(pos)
        print pos
        self.panel.PopupMenu(self.Menu4,pos)


if __name__ == "__main__":
    App = wx.App()
    Frame = MyFrame()
    Frame.Show()
    App.MainLoop()