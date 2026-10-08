import sqlite3

CAMINHO_BANCO = "banco/sistema_clientes.db"


def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)

    conexao.row_factory = sqlite3.Row

    return conexao