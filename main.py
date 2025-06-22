from database.database import DataBase

def main():
    db_manager = DataBase(initialize=False, create_views=False)
    db_manager.melhor_cliente()

if __name__ == "__main__":
    main()  