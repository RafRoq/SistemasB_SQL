from database.database import DataBase
import os

def main():
   # Instanciar o gerenciador do banco de dados
    db_manager = DataBase(initialize=False, create_views=False)

    # Caminho do arquivo SQL
    caminho_sql = os.path.join('queries', 'DDL', 'desempenhos_tenicos.sql')

    # Ler conteúdo do arquivo SQL
    #with open(caminho_sql, 'r', encoding='utf-8') as sql_file:
    #    sql_script = sql_file.read()

    # Executar o script de inserção de pacientes
    #cursor = db_manager.conn.cursor()
    #cursor.executescript(sql_script)
    #db_manager.conn.commit()
    #print("Pacientes deletados com sucesso.")

    query = db_manager.query_from_file(caminho_sql)
    df = db_manager.to_dataframe(query)
    print("\n")
    print("---------------------------------------------------------------------------------------------")
    print(df)
    print("---------------------------------------------------------------------------------------------")
    print("\n")
    """print("---------------------------------------------------------------------------------------------")
    print(df.tail())
    print("---------------------------------------------------------------------------------------------")
    print("\n")"""
    
if __name__ == "__main__":
    main()