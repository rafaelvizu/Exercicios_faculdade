import tkinter as tk
import sqlite3
import pandas as pd
import openpyxl
import pathlib
import win32com.client as win32
from os import path

conexao = sqlite3.connect('./clientes.db')
cursor = conexao.cursor()


cursor.execute(''' CREATE TABLE IF NOT EXISTS clientes (
     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     nome TEXT NOT NULL, 
     cpf TEXT(11) NOT NULL,
     email TEXT NOT NULL
     ) ''')

# confirmar a operacao
conexao.commit()


def cadastrar_cliente():
     #print('Cadastrando cliente', entrada_nome.get(), entrada_cpf.get(), len(entrada_email.get()))
     if (len(entrada_nome.get()) == 0 or len(entrada_cpf.get()) == 0 or len(entrada_email.get()) == 0):
          janela = tk.Tk()
          janela.title('Erro')
          label_erro = tk.Label(janela, text='Preencha todos os campos')
          label_erro.grid(row=0, column=0, padx=10, pady=10)

          button_ok = tk.Button(janela, text='OK', command=janela.destroy)
          button_ok.grid(row=1, column=0, padx=10, pady=10)
          janela.mainloop()
          return
    
     cursor.execute('INSERT INTO clientes (nome, cpf, email) VALUES (?, ?, ?)', (entrada_nome.get(), entrada_cpf.get(), entrada_email.get()))
     conexao.commit()

     entrada_nome.delete(0, tk.END)
     entrada_cpf.delete(0, tk.END)
     entrada_email.delete(0, tk.END)

def exportar_dados():
     cursor.execute('SELECT * FROM clientes')
     clientes = cursor.fetchall()

     df = pd.DataFrame(clientes, columns=['id', 'nome', 'cpf', 'email'])
     
     file_path = pathlib.Path('./clientes.xlsx')

     if not file_path.exists():
          workbook = openpyxl.Workbook()
          workbook.save(file_path)

     df.to_excel(file_path, index=False, header=True, sheet_name='clientes')
     
     full_path = path.abspath(file_path)
     
     excel = win32.gencache.EnsureDispatch('Excel.Application')
     excel.Visible = True
     wb = excel.Workbooks.Open(full_path)

janela = tk.Tk()
janela.title('Cadastro de Clientes')

# criar os labels
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_cpf = tk.Label(janela, text='CPF')
label_cpf.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='Email')
label_email.grid(row=2, column=0, padx=10, pady=10)

# entrada de dados
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=10, pady=10)

entrada_cpf = tk.Entry(janela)
entrada_cpf.grid(row=1, column=1, padx=10, pady=10)

entrada_email = tk.Entry(janela)
entrada_email.grid(row=2, column=1, padx=10, pady=10)

# botões 
botao_cadastrar = tk.Button(janela, text='Cadastrar', command=cadastrar_cliente)
botao_cadastrar.grid(row=3, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(janela, text='Exportar', command=exportar_dados)
botao_exportar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)


janela.mainloop()


# fechar a conexao  
conexao.close()