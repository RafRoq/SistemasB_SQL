import sqlite3
import os

class DataBase():

    DATABASE_NAME = 'database.db'
    SCHEMA_FILE = r'queries\scheme.sql'
    MIGRATIONS_DIR = r'queries\migrations'
    conn = None

    def __init__(self, initialize=True):
        self.get_database_connection()
        if initialize:
            self.initialize_database()

    def get_database_connection(self):
        self.conn = sqlite3.connect(self.DATABASE_NAME)
        self.conn.execute("PRAGMA foreign_keys = ON;")


    def initialize_database(self):
        if not os.path.exists(self.SCHEMA_FILE):
            print(f"Erro: Arquivo de esquema não encontrado em {self.SCHEMA_FILE}")
            return

        try:
            with open(self.SCHEMA_FILE, 'r', encoding='utf-8') as schema_file:
                schema_sql = schema_file.read()

            cursor = self.conn.cursor()
            cursor.executescript(schema_sql)

            self.conn.commit()
            print("Esquema do banco de dados criado/atualizado com sucesso.")

        except sqlite3.Error as e:
            print(f"Erro ao inicializar o banco de dados: {e}")
            self.conn.rollback()

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Conexão com o banco de dados fechada.")

# --- Como usar ---
if __name__ == "__main__":
    # Garanta que a pasta 'queries' exista no mesmo nível do seu script Python
    # E que 'schema.sql' esteja dentro de 'queries'
    
    # Exemplo de uso:
    db_manager = DataBase()

    # Você pode agora usar db_manager.conn para obter a conexão e interagir com o DB
    # Por exemplo:
    # cursor = db_manager.conn.cursor()
    # cursor.execute("INSERT INTO Paciente (nome, CPF) VALUES (?, ?)", ("João Silva", "12345678901"))
    # db_manager.conn.commit()
    # print("Paciente inserido.")

    # Não se esqueça de fechar a conexão ao final do seu programa
    db_manager.close_connection()