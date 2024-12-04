import sqlite3
from pathlib import Path

ROOt_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOt_PATH/ 'meu_banco.db')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("insert into clientes (nome,email) values (?,?)", ("teste 2", "teste2@gmail.com"))
    cursor.execute("insert into clientes (id, nome, email) values (?,?,?)", (2,"teste 3", "teste3@gmail.com"))
    conexao.commit()
except Exception as exc:
    print(f"Ops! um erro ocorreu!! {exc}")
    conexao.rollback()