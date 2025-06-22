from database.database import DataBase
import pandas as pd

def main():
    db_manager = DataBase(initialize=False)
    with open(r'queries\DML\melhor_cliente.sql', 'r', encoding='utf-8') as file:
        query = file.read()
        cursor = db_manager.conn.execute(query)
        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
        print(df.head())
        print(df.tail())
    with open(r'queries\DML\melhor_cliente.sql', 'r', encoding='utf-8') as file:
        query = file.read()
        cursor = db_manager.conn.execute(query)
        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
        print(df.head())
        print(df.tail())

if __name__ == "__main__":
    main()