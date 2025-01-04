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
        print("Conexiune reușită la baza de date!")
        return connection
    except Exception as e:
        print(f"Eroare la conectarea cu baza de date: {e}")
        return None
