from tkinter import Toplevel, Label, Entry, Button, messagebox
from app import add_person
import re
def validate_name(name):
    """Validate that the name contains only letters, spaces, or hyphens."""
    pattern = r"^[A-Za-z\s-]+$"  
    return re.match(pattern, name) is not None

def add_person_gui():
    """Add a person to the database after validating the inputs: length less than 100 characters, not null, and without special characters or numbers."""
    def save_person():
      firstname=firstname_entry.get()
      lastname=lastname_entry.get()
      if not firstname or not lastname:
         messagebox.showerror("Error","Please enter both firstname and lastname.")
         return
      if not validate_name(firstname):
        messagebox.showerror("Error","A valide name should contain only letters,spaces or hyphens.")
        return
      if not validate_name(lastname):
        messagebox.showerror("Error","A valide name should contain only letters,spaces or hyphens.")
        return
      if len(firstname) > 100:
            messagebox.showerror("Error", "Firstname must be shorter than 100 characters.")
            return
      if len(lastname) > 100:
            messagebox.showerror("Error", "Lastname must be shorter than 100 characters.")
            return
      
      try:
         add_person(firstname,lastname)
         messagebox.showinfo("Success",f"Person '{firstname} {lastname}' has been added.")
         firstname_entry.delete(0,"end")
         lastname_entry.delete(0,"end")
      except Exception as e:
         messagebox.showerror("Error",f"An error ocurred: {e}")
    window=Toplevel()
    window.geometry("400x300")
    window.title("Add Person")
    title_label = Label(window, text="Add person", font=("Helvetica", 25))
    title_label.pack(pady=20)
    Label(window,text="Firstname:",font=("Helvetica", 15)).pack(pady=5)
    firstname_entry=Entry(window,width=30)
    firstname_entry.pack(pady=10)
    Label(window,text="Lastname:",font=("Helvetica", 15)).pack(pady=5)
    lastname_entry=Entry(window,width=30)
    lastname_entry.pack(pady=5)
    Button(window,text="Save",command=save_person, font=("Helvetica", 10, "bold"), 
    width=10,                                           
    bg="lightblue",                 
    fg="black").pack(pady=10)
    

  