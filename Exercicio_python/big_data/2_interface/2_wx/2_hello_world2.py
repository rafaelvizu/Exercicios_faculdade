"""
Hello World, but with more meat.
"""

import wx

class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # vai pegar o construtor da classe pai, no caso, wx.Frame
        super(HelloFrame, self).__init__(*args, **kw)

        # criar uma painel para organizar os widgets
        pnl = wx.Panel(self)

        # criar dois textos estáticos e definir a fonte
        st = wx.StaticText(pnl, label="Hello World!")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)
        
        st2 = wx.StaticText(pnl, label="<3")
        font2 = st2.GetFont()
        font2.PointSize += 10
        st2.SetFont(font2)
        

        # vai criar um sizer para organizar os widgets no painel, no caso, na horizontal
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # vai adicionar uma borda de 25 px no painel - top e left
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        sizer.Add(st2, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

        # create a menu bar
        self.makeMenuBar()

        # vai criar o status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")


    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        
        # vamos criar um item de menu com um atalho de teclado, no caso, Ctrl-H
        # precisa ter um \t antes do atalho, e um & antes do texto do menu
        # o último parâmetro é o texto que vai aparecer na barra de status
        helloItem = fileMenu.Append(-1, "&Olá...\tCtrl-H",
                "Vai dizer olá pro usuário")
        
        # é uma linha separadora
        fileMenu.AppendSeparator()

        # wx.ID_EXIT é um ID padrão de wxWidgets para o item de menu Sair
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Agora vamos criar um menu de about
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Vamos criar a menu bar e adicionar os menus
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Vamos adicionar a menu bar na janela
        self.SetMenuBar(menuBar)

        # e agora vamos criar os eventos para os itens de menu
        # quando o usuário clicar em um item de menu, vai chamar o método
        # correspondente
        self.Bind(wx.EVT_MENU, self.OnOla, helloItem)
        self.Bind(wx.EVT_MENU, self.OnFechar,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAjuda, aboutItem)


    def OnFechar(self, event):
        """Close the frame, terminating the application."""
        wx.MessageBox("Saindo do programa...")
        self.Close(True)


    def OnOla(self, event):
        """Vai dizer olá pro usuário"""
        wx.MessageBox("Olá, usuário!")


    def OnAjuda(self, event):
        """Display an About Dialog"""
        wx.MessageBox("Este é um programa de exemplo de wxPython",
                      "Sobre o Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='Hello World 2')
    frm.Show()
    app.MainLoop()
