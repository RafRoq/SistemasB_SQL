from database.database import DataBase
import pandas as pd

def main():
    db_manager = DataBase(initialize=False, create_views=True)
    teste = pd.read_sql_query(db_manager.query_from_file(r'queries\DQL\desempenhos_tenicos.sql'), db_manager.conn)
    print(teste)
if __name__ == "__main__":
    main()