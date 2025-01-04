import psycopg2

DB_CONFIG = {
    'dbname': 'meeting_scheduler',
    'user': 'postgres',
    'password': 'sebi',
    'host': 'localhost',
    'port': '5432'
}

def get_db_connection():
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        print("The connection to the database was made succesfully!")
        return connection
    except Exception as e:
        print(f"Error: The connection to the database failed: {e}!")
        return None
