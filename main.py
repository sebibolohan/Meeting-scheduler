from db_connection import get_db_connection

if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        connection.close()
        print("Conexiunea a fost închisă.")
