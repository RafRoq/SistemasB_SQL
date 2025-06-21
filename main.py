from database.database import get_database_connection

def main():
    database = get_database_connection()
    database.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

if __name__ == "__main__":
    main()