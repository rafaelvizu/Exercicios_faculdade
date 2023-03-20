import wx
from controllers.ContatosController import ContatoController


class Home(wx.Frame):
     def __init__(self, parent, title):
          super(Home, self).__init__(parent, title=title, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
          self.SetSize((800, 600))
          self.Center()

          self.pnMain = wx.Panel(self)
          self.pnMain.SetSize((800, 600))
          self.pnMain.Center()
          self.contatosData = list()
          
          self.pnList = self.painelList()
          self.pnView = self.painelView()


          sizer = wx.BoxSizer(wx.HORIZONTAL)
          sizer.Add(self.pnList, 1, wx.CENTER | wx.EXPAND)
          sizer.Add(self.pnView, 1, wx.CENTER | wx.EXPAND)
          self.pnMain.SetSizer(sizer)

          self.btnAtt = wx.Button(self.pnView, -1, 'Atualizar', (10, 130))
          self.btnDelete = wx.Button(self.pnView, -1, 'Deletar', (100, 130))

          self.btnAtt.Bind(wx.EVT_BUTTON, self.onClickAtt, self.btnAtt)
          self.btnDelete.Bind(wx.EVT_BUTTON, self.onClickDelete, self.btnDelete)

     def painelList(self):
          painelList = wx.Panel(self.pnMain)
          painelList.SetSize((400, 300))


          self.lst = wx.ListBox(painelList, -1, (0, 0), (300, 200))
          self.lst.SetScrollbar(20, 1, 20, 1)

          self.atualizarLista()

          self.lst.Bind(wx.EVT_LISTBOX, self.onItemSelected)

          return painelList
     
     def painelView(self):
          painelView = wx.Panel(self.pnMain)
          painelView.SetSize((300, 200))

          self.lblNome = wx.StaticText(painelView, -1, 'Nome:', (10, 10))
          self.lblEmail = wx.StaticText(painelView, -1, 'Email:', (10, 40))
          self.lblTelefone = wx.StaticText(painelView, -1, 'Telefone:', (10, 70))
          self.lblDataNascimento = wx.StaticText(painelView, -1, 'Data de Nascimento:', (10, 100))

          return painelView
     
     def onItemSelected(self, event):
          for contato in self.contatosData:
               if (contato[0] == self.lst.GetClientData(self.lst.GetSelection())):

                    self.lblNome.SetLabel('Nome: ' + contato[1])
                    self.lblEmail.SetLabel('Email: ' + contato[2])
                    self.lblTelefone.SetLabel('Telefone: ' + contato[3])
                    self.lblDataNascimento.SetLabel('Data de Nascimento: ' + contato[4])
                    break
          

     def atualizarLista(self):
          self.lst.Clear()
          self.contatosData = ContatoController.buscarContatos()

          for contato in self.contatosData:
               self.lst.Append(contato[1])
               self.lst.SetClientData(self.lst.GetCount() - 1, contato[0])

     def onClickAtt(self, event):
          self.atualizarLista()

     def onClickDelete(self, event):
          if (self.lst.GetSelection() == -1):
               wx.MessageBox('Selecione um contato para deletar', 'Erro', wx.OK | wx.ICON_ERROR)
               return

          ContatoController.deletarContato(self.lst.GetClientData(self.lst.GetSelection()))
          self.atualizarLista()
    