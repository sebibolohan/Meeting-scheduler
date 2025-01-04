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
from tkinter import messagebox

def add_meeting(title, start_time, end_time, participants_input):
    """
    Add a meeting to the database and allow the user to confirm adding missing participants.

    Args:
        title (str): Meeting title.
        start_time (str): Start time of the meeting in 'YYYY-MM-DD HH:MM' format.
        end_time (str): End time of the meeting in 'YYYY-MM-DD HH:MM' format.
        participants (list): List of participants (Firstname Lastname).
    """
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        participants = [p.strip() for p in participants_input.split(",")]
        for participant in participants:
            firstname, lastname = participant.split(" ", 1)

            cursor.execute(
                "SELECT id FROM persons WHERE first_name = %s AND last_name = %s",
                (firstname, lastname),
            )
            result = cursor.fetchone()

            if not result:
                add_now = messagebox.askyesno(
                    "Participant Not Found",
                    f"Participant '{participant}' does not exist. Would you like to add them now?"
                )
                if add_now:
                   
                    cursor.execute(
                        "INSERT INTO persons (first_name, last_name) VALUES (%s, %s) RETURNING id",
                        (firstname, lastname),
                    )
                    print(f"Participant '{participant}' has been added.")
                else:
                    messagebox.showinfo(
                        "Meeting Creation Cancelled",
                        f"Meeting creation has been cancelled because participant '{participant}' was not added."
                    )
                    connection.rollback()  
                    return

        cursor.execute(
            "INSERT INTO meetings (title, start_time, end_time) VALUES (%s, %s, %s) RETURNING id",
            (title, start_time, end_time),
        )
        meeting_id = cursor.fetchone()[0] 

        for participant in participants:
            firstname, lastname = participant.split(" ", 1)

            cursor.execute(
                "SELECT id FROM persons WHERE first_name = %s AND last_name = %s",
                (firstname, lastname),
            )
            person_id = cursor.fetchone()[0]

            cursor.execute(
                "INSERT INTO meeting_participants (meeting_id, person_id) VALUES (%s, %s)",
                (meeting_id, person_id),
            )

        connection.commit()
        print(f"Meeting '{title}' and its participants have been successfully added.")
        messagebox.showinfo("Success", f"Meeting '{title}' has been added.")

    except Exception as e:
        print(f"Error adding meeting: {e}")
        if 'connection' in locals() and connection:
            connection.rollback()  
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()
