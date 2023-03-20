import wx
from views.HomeFrame import Home
from views.CreateContatoFrame import CreateContato


class App(wx.App):
     def OnInit(self):
          self.frame = Home(None, 'Agenda')
          self.novoContato = None
          self.frame.Show()
          self.menuBar()
          return True
     
     def menuBar(self):
          menuBar = wx.MenuBar()
          menu = wx.Menu()
          novoContatoItem = menu.Append(-1, '&Novo Contato\tCtrl+N')
          menuBar.Append(menu, 'Contato')

          menu.AppendSeparator()

          menu.Append(wx.ID_EXIT, '&Sair\tCtrl+Q')

          self.frame.SetMenuBar(menuBar)
          self.frame.Bind(wx.EVT_MENU, self.onExit, id=wx.ID_EXIT)
          self.frame.Bind(wx.EVT_MENU, self.onNewContact, id=novoContatoItem.GetId())

     def onExit(self, event):
          if (self.novoContato):
               self.novoContato.Close()
          
          self.frame.Close()
     
     def onNewContact(self, event):
          self.novoContato = CreateContato(None, title='Novo Contato')
          self.novoContato.Show()
     

if __name__ == "__main__":
     app = App()
     app.MainLoop()