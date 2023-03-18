import wx

# Um aplicativo wxPython não tem um procedimento principal; o equivalente é o wx. Membro AppConsole.OnInit definido para uma classe derivada de wx. Aplicativo.

# O OnInit geralmente cria uma janela superior no mínimo. Ao contrário de em versões anteriores do wxPython, o OnInit não retorna um quadro. Em vez disso, ele retorna um valor booleano que indica se o processamento deve continuar () ou não ().TrueFalse

# Um aplicativo é fechado destruindo todas as janelas. Porque todos os quadros deve ser destruído para o aplicativo sair, é aconselhável usar quadros pai sempre que possível ao criar novos quadros, de modo que a exclusão do quadro de nível superior excluirá automaticamente os quadros filho. A alternativa é excluir explicitamente quadros filho no nível superior wx do quadro. Manipulador CloseEvent.

# Em emergências o wx. A função de saída pode ser chamada para matar o no entanto, normalmente o aplicativo é desligado automaticamente quando a última janela de nível superior for fechada. Consulte Desligamento do aplicativo.

class DeviceApp(wx.App):
    
    def OnInit(self):
        the_frame = wx.Frame(None, -1)

        the_frame.Show(True)
        return True
    

print(DeviceApp().OnInit())