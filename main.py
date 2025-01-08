from db_connection import get_db_connection
import tkinter as tk
from tkinter import messagebox
from gui import add_person_gui,add_meeting_gui, view_meetings_gui,export_meetings_gui,import_meetings_gui
def exit_app():
    if messagebox.askyesno("Exit", "Are you sure that you want to close the app?"):
        root.destroy()

#Testing the connection with the database
connection = get_db_connection()
if not connection:
    print("Error: The connection to the database failed!")
    exit()  
else:
    print("The connection to the database was made succesfully!")
    connection.close()

#Open the GUI
root = tk.Tk()
root.title("Meeting Scheduler")
root.geometry("600x550")
root.configure(bg='#D2B48C')
title_label = tk.Label(root, text="Meeting Scheduler", font=("Helvetica", 30),background="#D2B48C")
title_label.pack(pady=20)

tk.Button(
    root, 
    text="Add Person", 
    command=add_person_gui, 
    font=("Helvetica", 12, "bold"), 
    width=20,                      
    height=2,                       
    bg="lightgrey",                 
    fg="black",                 
).pack(pady=10)
tk.Button(
    root, 
    text="Add Meeting", 
    command=add_meeting_gui, 
    font=("Helvetica", 12, "bold"), 
    width=20,                      
    height=2,                       
    bg="lightgrey",                 
    fg="black",                 
).pack(pady=10)
tk.Button(
    root,
    text="View Meetings",
    command=view_meetings_gui,
    font=("Helvetica", 12, "bold"), 
    width=20,                      
    height=2,                       
    bg="lightgrey",                 
    fg="black", ).pack(pady=10)
tk.Button(
    root,
    text="Export as .ics",
    command=export_meetings_gui,
    font=("Helvetica", 12, "bold"), 
    width=20,                      
    height=2,                       
    bg="lightgrey",                 
    fg="black", ).pack(pady=10)
tk.Button(
    root,
    text="Import as .ics",
    command=import_meetings_gui,
    font=("Helvetica", 12, "bold"), 
    width=20,                      
    height=2,                       
    bg="lightgrey",                 
    fg="black", ).pack(pady=10)
tk.Button(
    root,
    text="Exit",
    command=exit_app,
    font=("Helvetica", 12, "bold"), 
    width=20,                      
    height=2,                       
    bg="lightgrey",                 
    fg="black", ).pack(pady=10)
# Start loop Tkinter
if __name__ == "__main__":
    root.mainloop()
