import wx
from controllers.ContatosController import ContatoController

class CreateContato(wx.Frame):
    
     def __init__(self, *args, **kw):
          super().__init__(*args, **kw, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
          self.SetSize((600, 400))

          self.pnMain = wx.Panel(self)
          self.pnMain.SetBackgroundColour('#FFFFFF')
          self.pnMain.SetSize((600, 400))
          
          self.createPainel()
     


     def createPainel(self):
          self.pnInput = wx.Panel(self.pnMain, size=(600, 300))          

          self.lblNome = wx.StaticText(self.pnInput, label='Nome', pos=(10, 10))
          self.txtNome = wx.TextCtrl(self.pnInput, pos=(10, 30), size=(500, 30))

          self.lblEmail = wx.StaticText(self.pnInput, label='Email', pos=(10, 70))
          self.txtEmail = wx.TextCtrl(self.pnInput, pos=(10, 90), size=(500, 30))

          self.lblTelefone = wx.StaticText(self.pnInput, label='Telefone', pos=(10, 130))
          self.txtTelefone = wx.TextCtrl(self.pnInput, pos=(10, 150), size=(500, 30))

          self.lblDataNascimento = wx.StaticText(self.pnInput, label='Data de Nascimento', pos=(10, 190))
          self.txtDataNascimento = wx.TextCtrl(self.pnInput, pos=(10, 210), size=(500, 30))



          self.pnButtons = wx.Panel(self.pnMain, size=(600, 100), pos=(0, 300))
          self.pnButtons.SetBackgroundColour('#FFFFFF')

          self.btnSalvar = wx.Button(self.pnButtons, label='Salvar', pos=(10, 10), size=(500, 30))
          self.btnSalvar.Bind(wx.EVT_BUTTON, self.onSave)
     
     

     def onSave(self, event):
          status = ContatoController.novoContato(self.txtNome.GetValue(), 
                                                 self.txtEmail.GetValue(), 
                                                 self.txtTelefone.GetValue(), 
                                                 self.txtDataNascimento.GetValue())
          if status:
               return self.Close()



     def onCancel(self, event):
          wx.MessageBox('Deseja realmente cancelar?', 'Cancelar', wx.YES_NO | wx.ICON_QUESTION)
          self.Close()
