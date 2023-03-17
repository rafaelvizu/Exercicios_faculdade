from db.dbConn import Database as db
import pandas as pd
import datetime

db.createTable('services', '''
          id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
          name TEXT NOT NULL,
          description TEXT,
          price REAL NOT NULL,
          status TEXT NOT NULL,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
''')

class Services:
     @staticmethod
     def create(name, description, price, status):
          try:
               db.static_cur.execute(f'INSERT INTO services (name, description, price, status) VALUES ("{name}", "{description}", "{price}", "{status}") ')
               db.static_conn.commit()
               print(f'Serviço {name} criado com sucesso!')
               return True
          except:
               print(f'Erro ao criar o serviço {name}!')
               return False

     @staticmethod
     def read():
          try:
               db.static_cur.execute('SELECT * FROM services')
               servicos = db.static_cur.fetchall()     
               return pd.DataFrame(servicos, columns=['id', 'name', 'description', 'price', 'status', 'created_at'])
          except:
               print('Erro ao ler os serviços!')
               return False

     @staticmethod
     def update(id, name, description, price, status):
          try:
               db.static_cur.execute(f'UPDATE services SET name="{name}", description="{description}", price="{price}", status="{status}" WHERE id={id}')
               db.static_conn.commit()
               print(f'Serviço {name} atualizado com sucesso!')
               return True
          except:
               print(f'Erro ao atualizar o serviço {name}!')
               return False

     @staticmethod
     def delete(id):
          try:
               db.static_cur.execute(f'DELETE FROM services WHERE id={id}')
               db.static_conn.commit()
               print(f'Serviço {id} deletado com sucesso!')
               return True
          except:
               print(f'Erro ao deletar o serviço {id}!')
               return False
     