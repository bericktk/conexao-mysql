import mysql.connector
from mysql.connector import errorcode

class Conexao:
  def __init__(self, host, user, password, database):
    self.host = host
    self.user = user
    self.password = password
    self.database = database

  def conectar(self):
    try:
      self.con = mysql.connector.connect(
        host = self.host,
        user = self.user,
        password = self.password,
        database = self.database
      )

      self.cursor = self.con.cursor()
      print(f'Conexão com o  banco de dados {self.database} realizada com sucesso!')
    
    except mysql.connector.Error as error:
      print(f'Falha ao conectar ao banco de dados {self.database}: {error}')

  def criarTabela(self, tabela):
    try:
      self.cursor.execute(
        f"""CREATE TABLE IF NOT EXISTS {tabela}(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        cpf  VARCHAR(15) NOT NULL,
        email VARCHAR(100) NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        turma  VARCHAR(20) NOT NULL
        );"""
      )

      print(f'Tabela {tabela} criada com sucesso!')

    except mysql.connector.Error as error:
      print(f"Falha ao criar a tabela {tabela}: {error}")

  def adicionarValores(self, nome, cpf, email, telefone, turma):
    try:
      self.cursor.execute("""INSERT INTO alunos(nome, cpf, email, telefone, turma) VALUES (%s, %s, %s, %s ,%s)""",(nome, cpf, email, telefone, turma))
      self.con.commit()
      print('Dados adicionados com sucesso!')

    except mysql.connector.Error as error:
      print(f"Falha ao inserir os dados na tabela: {error}")

  def fecharConexao(self):
    if self.con.is_connected():
        self.con.close()
        print("Conexão fechada.")