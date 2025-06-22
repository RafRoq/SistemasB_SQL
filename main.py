from database.database import DataBase
import pandas as pd

def main():
    db_manager = DataBase(initialize=False, create_views=False)
    teste = pd.read_sql_query(db_manager.query_from_file(r'queries\DQL\devedores.sql'), db_manager.conn)
        
if __name__ == "__main__":
    main()