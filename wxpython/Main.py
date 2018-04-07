#coding=utf-8

import wx

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self,None,-1,"多模测试热补丁工具",size = (800,600))
        panel = wx.Panel(self)
        self.checkbox1 = wx.CheckBox(panel,-1,"CCC",(60,20),(200,20))                    #复选框1
        self.checkbox2 = wx.CheckBox(panel, -1, "CCF0",(60,40),(200,20))                 #复选框2
        self.checkbox3 = wx.CheckBox(panel, -1, "CCE1",(60,60),(200,20))                 #复选框3
        self.checkbox4 = wx.CheckBox(panel, -1, "全选",(60,80),(200,20))                 # 复选框4
        self.checkbox1.Bind(wx.EVT_CHECKBOX,self.One_Play)
        self.checkbox2.Bind(wx.EVT_CHECKBOX, self.Two_Play)
        self.checkbox4.Bind(wx.EVT_CHECKBOX, self.End_Play)

    def One_Play(self,event):
        print "本次选择了吗：",self.checkbox1.GetValue()

    def Two_Play(self,event):
        print "本次选择了吗：", self.checkbox2.GetValue()

    def End_Play(self,event):
        valuelist = list()
        valuelist.append(self.checkbox1.GetLabel())
        valuelist.append(self.checkbox2.GetLabel())
        valuelist.append(self.checkbox3.GetLabel())
        print valuelist

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
