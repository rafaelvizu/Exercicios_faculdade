import wx


class CreateContato(wx.Frame):
    
     def __init__(self, *args, **kw):
          super().__init__(*args, **kw, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
          self.SetSize((1000, 1000))
          
          self.pnMain = wx.Panel(self)
          self.pnMain.SetSize((1000, 1000))


          self.pnInput = self.createInputPainel()
          #self.pnButtons = self.createButtonsPainel()


     def createInputPainel(self):
          pnInput = wx.Panel(self.pnMain)
          pnInput.SetSize((400, 300))
          pnInput.BackgroundColour = 'red'

          lblNome = wx.StaticText(pnInput, 1, 'Nome:')
          lblEmail = wx.StaticText(pnInput, 10, 'Email:')


          return pnInput

     def createButtonsPainel(self):
          pnButtons = wx.Panel(self.pnMain)
          pnButtons.SetSize((400, 300))

          btnSalvar = wx.Button(pnButtons, -1, 'Salvar')
          btnCancelar = wx.Button(pnButtons, -1, 'Cancelar')


          self.Bind(wx.EVT_BUTTON, self.onSave, btnSalvar)
          self.Bind(wx.EVT_BUTTON, self.onCancel, btnCancelar)

          return pnButtons
     

     def onSave(self, event):
          print('Salvando contato...')
          self.Close()

     def onCancel(self, event):
          wx.MessageBox('Deseja realmente cancelar?', 'Cancelar', wx.YES_NO | wx.ICON_QUESTION)
          self.Close()


if __name__ == '__main__':
     app = wx.App()
     frm = CreateContato(None, title='Criar Contato')
     frm.Show()
     app.MainLoop()