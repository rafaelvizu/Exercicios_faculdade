import wx


class Home(wx.Frame):
     def __init__(self, parent, title):
          super(Home, self).__init__(parent, title=title, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
          self.SetSize((800, 600))
          self.Center()

          self.pnMain = wx.Panel(self)
          self.pnMain.SetSize((800, 600))
          self.pnMain.Center()
          
          self.pnList = self.painelList()
          self.pnView = self.painelView()


          sizer = wx.BoxSizer(wx.HORIZONTAL)
          sizer.Add(self.pnList, 1, wx.CENTER | wx.EXPAND)
          sizer.Add(self.pnView, 1, wx.CENTER | wx.EXPAND)
          self.pnMain.SetSizer(sizer)

     def painelList(self):
          painelList = wx.Panel(self.pnMain)
          painelList.SetSize((400, 300))


          lst = wx.ListBox(painelList, -1, (0, 0), (300, 200))
          lst.SetScrollbar(20, 1, 20, 1)

          lst.Append('Item 1')
          lst.Append('Item 2')
          lst.Append('Item 3')
          return painelList
     
     def painelView(self):
          painelView = wx.Panel(self.pnMain)
          painelView.SetSize((300, 200))

          self.lblNome = wx.StaticText(painelView, -1, 'Nome:', (10, 10))
          self.lblEmail = wx.StaticText(painelView, -1, 'Email:', (10, 40))
          self.lblEndereco = wx.StaticText(painelView, -1, 'Endereço:', (10, 70))
          self.lblTelefone = wx.StaticText(painelView, -1, 'Telefone:', (10, 100))
          self.lblDataNascimento = wx.StaticText(painelView, -1, 'Data de Nascimento:', (10, 130))

          return painelView
     
