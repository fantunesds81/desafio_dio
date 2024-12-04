import sqlite3
from pathlib import Path

ROOt_PATH = Path(__file__).parent

conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

def criar_tabela(cursor):
    cursor.excute(

        ('CREATE TABLE clientes(id integer primary key autoincrement, nome varchar(100), email varchar(150))')

    )
    conexao.commit()


def inserir_registro(conexao,cursor,nome,email):
    data = ('fabio','fantunesds@gmail.com')
    cursor.execute('insert into clientes (nome,email) values (?,?);', data)
    conexao.commit()

def atualizar_registro(conexao,cursor,nome,email,id):
    data = (nome,email,id)
    cursor.execute('update clientes set nome=?, email=? where id=?', data)
    conexao.commit()

def excluir_registro(conexao,cursor,id):
    data = (id,)
    cursor.execute('delete from clientes where id=?;',data)
    conexao.commit()

def inserir_muitos(conexao,cursor,dados):
    cursor.executemany("insert into clientes (nome,email) values (?,?)", dados)
    conexao.commit()

dados = [
    ('guilherme','guilherme@gmail.com'),
    ('cuzinho', 'lindo@gmail.com'),
    ('chota','chota@gmail.com'),
]


def recuperar_cliente(cursor,id):
    cursor.execute("select * from clientes where id=?",(id,))
    return cursor.fetchone()

def listar_cliente(cursor):
    return cursor.execute("select * from clientes;")


cliente = recuperar_cliente(cursor, 1)
print(cliente)

clientes = listar_cliente(cursor)
for cliente in clientes:
    print(cliente)

#inserir_muitos(conexao,cursor,dados)
#atualizar_registro(conexao,cursor, "fabio antunes", "fantunesds@outlook.com", 1)
#excluir_registro(conexao,cursor, 1)


