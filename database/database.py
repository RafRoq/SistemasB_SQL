from  sqlite4  import  SQLite4

def get_database_connection():
    """Create a connection to the SQLite database."""
    database = SQLite4('database.db')
    database.connect()
    return database