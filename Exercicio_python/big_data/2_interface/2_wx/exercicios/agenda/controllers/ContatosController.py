from models.ContatosModel import Contatos
import wx


class ContatoController:

     @staticmethod
     def novoContato(nome, telefone, email, data_nascimento):
          if len(nome) == 0 or len(telefone) == 0:
               wx.MessageBox('Preencha os campos obrigatórios', 'Erro', wx.OK | wx.ICON_ERROR)
               return False
          
          try:
               Contatos(nome, telefone, email, data_nascimento).save()
               wx.MessageBox('Contato salvo com sucesso', 'Sucesso', wx.OK | wx.ICON_INFORMATION)
               return True
          except Exception as e:
               print(e)
               wx.MessageBox('Erro ao salvar contato', 'Erro', wx.OK | wx.ICON_ERROR)
               return False

     @staticmethod
     def buscarContatos():
          try:
               contatos =  Contatos.all()

               if len(contatos) == 0:
                    wx.MessageBox('Nenhum contato encontrado', 'Erro', wx.OK | wx.ICON_ERROR)
               
               return contatos
          except Exception as e:
               wx.MessageBox('Erro ao buscar contatos', 'Erro', wx.OK | wx.ICON_ERROR)
               return list()
     
     @staticmethod
     def buscarContato(id):
          try:
               contato = Contatos.find(id)
               return contato
          except Exception as e:
               wx.MessageBox('Erro ao buscar contato', 'Erro', wx.OK | wx.ICON_ERROR)
               return None
     

     @staticmethod
     def deletarContato(id):
          try:
               Contatos.delete(id)
               wx.MessageBox('Contato deletado com sucesso', 'Sucesso', wx.OK | wx.ICON_INFORMATION)
          except Exception as e:
               wx.MessageBox('Erro ao deletar contato', 'Erro', wx.OK | wx.ICON_ERROR)
               return False
