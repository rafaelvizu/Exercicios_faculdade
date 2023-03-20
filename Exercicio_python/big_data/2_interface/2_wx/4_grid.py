import wx
import wx.grid


class GridFrame(wx.Frame):
     def __init__(self, parent, title):
          wx.Frame.__init__(self, parent, title=title, size=(600, 400))
        
          grid = wx.grid.Grid(self, -1)
          grid.CreateGrid(100, 10)


          # podemos definir o tamanho de linhas e colunas de forma individual
          grid.SetRowSize(0, 60)
          grid.SetColSize(0, 120)


          # E defina o conteúdo da célula da grade como strings
          grid.SetCellValue(0, 0, 'Hello, wxPython grid world!')
          
          # Podemos especificar quee algumas células são read.only
          grid.SetCellValue(0, 3, 'This is read.only')
          grid.SetReadOnly(0, 3)


          # As cores podem ser especificadas para o conteúdo da célula da grade
          grid.SetCellValue(3, 3, 'green on grey')
          grid.SetCellTextColour(3, 3, wx.GREEN)
          grid.SetCellBackgroundColour(3, 3, wx.LIGHT_GREY)

          # Podemos especificar que algumas células armazenarão valores numéricos
          # valores em vez de strings. Aqui definimos a coluna da grade 5 
          # para manter valores de ponto flutuante exibidos com largura de 6
          # e precisão de 2
          grid.SetColFormatFloat(5, 6, 2)
          grid.SetCellValue(0, 5, '3.1415926535')




if __name__ == '__main__':
     app = wx.App()
     frame = GridFrame(None, 'Grid')
     frame.Show()
     app.MainLoop()