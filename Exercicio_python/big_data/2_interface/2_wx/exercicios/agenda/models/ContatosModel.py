from db.Conn import Connection

Connection.createTable('contatos', 'id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT, telefone TEXT NOT NULL, data_nascimento TEXT')

class Contatos:
     def __init__(self, nome, telefone, email, data_nascimento):
          self.nome = nome
          self.email = email
          self.telefone = telefone
          self.data_nascimento = data_nascimento
     
     def save(self):
          try:
               Connection.getCursor().execute(f"INSERT INTO contatos (nome, email, telefone, data_nascimento) VALUES ('{self.nome}', '{self.email}', '{self.telefone}', '{self.data_nascimento}')")
               Connection.getConn().commit()
          except Exception as e:
               print('Error ao salvar contato: ', e)

     @staticmethod
     def all():
          try:
               Connection.getCursor().execute("SELECT * FROM contatos")
               return Connection.getCursor().fetchall()
          except Exception as e:
               print('Error ao buscar contatos: ', e)

     @staticmethod
     def find(id):
          try:
               Connection.getCursor().execute(f"SELECT * FROM contatos WHERE id = {id}")
               return Connection.getCursor().fetchone()
          except Exception as e:
               print('Error ao buscar contato: ', e)

     @staticmethod
     def delete(id):
          try:
               Connection.getCursor().execute(f"DELETE FROM contatos WHERE id = {id}")
               Connection.getConn().commit()
          except Exception as e:
               print('Error ao deletar contato: ', e)

     @staticmethod
     def update(id, nome, email, telefone, data_nascimento):
          try:
               Connection.getCursor().execute(f"UPDATE contatos SET nome = '{nome}', email = '{email}', telefone = '{telefone}', data_nascimento = '{data_nascimento}' WHERE id = {id}")
               Connection.getConn().commit()
          except Exception as e:
               print('Error ao atualizar contato: ', e)
    