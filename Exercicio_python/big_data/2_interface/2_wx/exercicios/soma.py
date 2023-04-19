import wx


class SomaFrame(wx.Frame):
     def __init__(self, *args, **kw):
          super().__init__(*args, **kw, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
          self.SetSize((500, 100)) 

          pnMain = wx.Panel(self)

          # input painel
          
          # input 1
          self.input1 = wx.TextCtrl(pnMain, style=wx.TE_RIGHT)
          self.input1.SetFont(wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL))
          self.input1.SetBackgroundColour('white')
          self.input1.SetForegroundColour('black')
          self.input1.SetSize((100, 30))
          

          self.somaText = wx.StaticText(pnMain, label='+',size=(20, 30))
          self.somaText.SetFont(wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL))

          # input 2
          self.input2 = wx.TextCtrl(pnMain, style=wx.TE_RIGHT)
          self.input2.SetFont(wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL))
          self.input2.SetBackgroundColour('white')
          self.input2.SetForegroundColour('black')
          self.input2.SetSize((100, 30))


          self.outputText = wx.StaticText(pnMain, label='=',size=(20, 30))
          self.outputText.SetFont(wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL))

          # output painel
          self.output = wx.TextCtrl(pnMain, style=wx.TE_RIGHT)
          self.output.SetFont(wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL))
          self.output.SetBackgroundColour('white')
          self.output.SetForegroundColour('black')
          self.output.SetSize((100, 30))
          self.output.Disable()


          sizerInput = wx.BoxSizer(wx.HORIZONTAL)
          sizerInput.Add(self.input1, 0, wx.ALL, 5)
          sizerInput.Add(self.somaText, 0, wx.ALL, 5)
          sizerInput.Add(self.input2, 0, wx.ALL, 5)
          sizerInput.Add(self.outputText, 0, wx.ALL, 5)
          sizerInput.Add(self.output, 0, wx.ALL, 5)
          pnMain.SetSizer(sizerInput)


          self.Bind(wx.EVT_TEXT, self.OnSoma, self.input1)
          self.Bind(wx.EVT_TEXT, self.OnSoma, self.input2)

          
     def OnSoma(self, event):
          try:
               input1 = self.input1.GetValue()
               input2 = self.input2.GetValue()
               output = int(input1) + int(input2)
               self.output.SetValue(str(output))
          except:
               self.output.SetValue('')
          

     



class App(wx.App):
     def OnInit(self):
          self.frame = SomaFrame(None, title='Soma')
          self.menuBar()
          self.frame.Show()
          return True
     
     def menuBar(self):
          menuBar = wx.MenuBar()
          menuFile = wx.Menu()
          menuBar.Append(menuFile, '&File')
          menuFile.Append(wx.ID_EXIT, '&Exit')
          self.frame.SetMenuBar(menuBar)
          self.frame.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
    

     def OnExit(self, event):
          self.frame.Close()


if __name__ == '__main__':
    app = App()
    app.MainLoop()