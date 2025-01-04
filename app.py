from db_connection import get_db_connection
def add_person (firstname, lastname):
    try:
        connection=get_db_connection()
        cursor=connection.cursor()
        cursor.execute("INSERT INTO persons (first_name, last_name) VALUES (%s,%s)", (firstname,lastname,))
        connection.commit()
        print(f"Person '{firstname} {lastname}' was added in the table persons successfully.")
    except Exception as e:
        print(f"Error at adding person: {e}")
    finally:
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()