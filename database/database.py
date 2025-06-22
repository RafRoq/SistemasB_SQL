import sqlite3
import os

class DataBase():

    DATABASE_NAME = 'database.db'
    SCHEMA_FILE = r'queries\scheme.sql'
    MIGRATIONS_DIR = r'queries\migrations'
    VIEWS_DIR = r'queries\views'
    conn = None

    def __init__(self, initialize=True, create_views=True):
        self._get_database_connection()
        if initialize:
            self._initialize_database()
        if create_views:
            self.create_views()

    def _get_database_connection(self):
        self.conn = sqlite3.connect(self.DATABASE_NAME)
        self.conn.execute("PRAGMA foreign_keys = ON;")

    def create_views(self):
        sql_files = [f for f in os.listdir(self.VIEWS_DIR) if f.endswith('.sql')]
        if not sql_files:
            print("Nenhum arquivo de view encontrado na pasta 'views'.")
            return
        for sql_file in sql_files:
            file_path = os.path.join(self.VIEWS_DIR, sql_file)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    view_sql = file.read()
                cursor = self.conn.cursor()
                cursor.execute(view_sql)
                self.conn.commit()
                print(f"View '{sql_file}' criada com sucesso.")
            except sqlite3.Error as e:
                print(f"Erro ao criar view '{sql_file}': {e}")
                self.conn.rollback()

    def _initialize_database(self):
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

    def list_views(self):
        cursor = self.conn.execute("SELECT name FROM sqlite_master WHERE type='view';")
        views = cursor.fetchall()
        return [view[0] for view in views]
    
    def melhor_cliente(self):
        try:
            cursor = self.conn.execute("SELECT * FROM melhor_cliente;")
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"Erro ao obter o melhor cliente: {e}")
            return []

# database.py

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