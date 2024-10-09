from conexao import *
from dados import *

# Conectando ao Banco de Dados Escola
banco_escola = Conexao(host, user, password, database)
banco_escola.conectar()

# Criando a Tabela Aluno caso não exista
tabela = input('Digite o nome da tabela que deseja inserir os dados: ')
banco_escola.criarTabela(tabela)

# Adicionando valores a tabela
nome = input('Digite seu nome: ')
cpf = input('Digite seu cpf: ')
email = input('Digite seu email: ')
telefone = input('Digite seu telefone: ')
turma = input('Digite seu turma: ')

banco_escola.adicionarValores(nome, cpf, email, telefone, turma)

# Fechando a conexão
banco_escola.fecharConexao()