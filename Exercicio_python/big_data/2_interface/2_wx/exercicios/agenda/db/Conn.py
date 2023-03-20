import sqlite3


class Connection:
     _staticConn = sqlite3.connect('./db/database.db')
     _staticCursor = _staticConn.cursor()


     @staticmethod
     def getConn():
          return Connection._staticConn
     
     @staticmethod
     def getCursor():
          return Connection._staticCursor
     
     @staticmethod
     def createTable(name, columns):
          try:
               Connection._staticCursor.execute(f"CREATE TABLE IF NOT EXISTS {name} ({columns})")
               Connection._staticConn.commit()
          except Exception as e:
               print('Error ao criar tabela: ', e)

     @staticmethod
     def close():
          Connection._staticConn.close()
