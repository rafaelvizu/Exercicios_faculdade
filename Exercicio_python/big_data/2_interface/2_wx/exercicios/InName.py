import wx

class InputFrame(wx.Frame):
    
     def __init__(self, *args, **kw):
          super().__init__(*args, **kw)

          pn1 = wx.Panel(self)


          self.st1 = wx.StaticText(pn1, label="Nome:")
          self.tc1 = wx.TextCtrl(pn1)
          self.btn1 = wx.Button(pn1, label="Ok")
          self.btn1.Bind(wx.EVT_BUTTON, self.OnClick)
          self.sh1 = wx.StaticText(pn1, label="")

          font = self.st1.GetFont()
          font.PointSize += 10
          font = font.Bold()
          self.st1.SetFont(font)

          sizer = wx.BoxSizer(wx.VERTICAL)
          sizer.Add(self.st1, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
          sizer.Add(self.tc1, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
          sizer.Add(self.btn1, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
          sizer.Add(self.sh1, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
          pn1.SetSizer(sizer)

          
     def OnClick(self, event):
          self.sh1.SetLabel(self.tc1.GetValue())


if __name__ == '__main__':
     app = wx.App()
     frm = InputFrame(None, title='Input Name')
     frm.Show()
     app.MainLoop()