import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class Dados:
     def __init__(self, data):
          self.root = tk.Tk()
          self.root.title("Dados")
          self.root.geometry("300x300")
          #self.root.resizable(False, False)
          self.root.configure(bg="#000000")
          
          if not data.empty:
               self.criarGrafico(data)
     

          self.root.mainloop()

     def criarGrafico(self, data):
          graph = plt.Figure(figsize=(10, 10), dpi=100)
          ax1 = graph.add_subplot(111)
          bar1 = FigureCanvasTkAgg(graph, self.root)

          bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)          
          data = data.head().sort_values(by='price', ascending=False)

          ax1.bar(data['name'], data['price'], color='blue')
          #data.plot(kind='bar', legend=True, ax=ax1)
     

          ax1.set_title('Serviços')
          ax1.set_xlabel('Nome')
          ax1.set_ylabel('Preço: R$')