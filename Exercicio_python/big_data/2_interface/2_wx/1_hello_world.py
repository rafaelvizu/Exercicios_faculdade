import wx


a = wx.App()
frame = wx.Frame(None, title="Hello World")
label = wx.StaticText(frame, label="Hello World")
frame.Show()



a.MainLoop()