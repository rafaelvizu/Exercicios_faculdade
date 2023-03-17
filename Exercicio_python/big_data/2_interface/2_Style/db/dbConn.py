import sqlite3


class Database:
     static_conn = sqlite3.connect('./db/database.db')
     static_cur = static_conn.cursor()

     @staticmethod
     def createTable(table, columns):
          try:
               Database.static_cur.execute(f'CREATE TABLE IF NOT EXISTS {table} ({columns})')
               Database.static_conn.commit()

               print(f'Tabela {table} criada com sucesso!')
               return True
          except:
               print(f'Erro ao criar a tabela {table}!')
               return False

     @staticmethod
     def closeConnection():
          Database.conn.close()

