from database.database import DataBase
import pandas as pd

def main():
    db_manager = DataBase(initialize=False, create_views=False)
    teste = db_manager.to_dataframe(db_manager.query_from_file(r'queries\DQL\desempenhos_tenicos.sql'))
    print(teste)
if __name__ == "__main__":
    main()