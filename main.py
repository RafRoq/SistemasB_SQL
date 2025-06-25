from database.database import DataBase
import os

def main():
   # Instanciar o gerenciador do banco de dados
    db_manager = DataBase(initialize=False, create_views=False)

    # Caminho do arquivo SQL
    caminho_sql = os.path.join('queries', 'DML', 'deletar_paciente.sql')

    # Ler conteúdo do arquivo SQL
    with open(caminho_sql, 'r', encoding='utf-8') as sql_file:
        sql_script = sql_file.read()

    # Executar o script de inserção de pacientes
    cursor = db_manager.conn.cursor()
    cursor.executescript(sql_script)
    db_manager.conn.commit()
    print("Pacientes deletados com sucesso.")

if __name__ == "__main__":
    main()