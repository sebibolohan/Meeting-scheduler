from tkinter import Toplevel, Label, Entry, Button, messagebox
from app import add_person,add_meeting
from datetime import datetime
import re
def validate_name(name):
    """Validate that the name contains only letters, spaces, or hyphens."""
    pattern = r"^[A-Za-z\s-]+$"  
    return re.match(pattern, name) is not None

def validate_datetime(datetime_string):
    """Validate if a string is in the format 'YYYY-MM-DD HH:MM' and is a valid date and time."""
    try:
        datetime.strptime(datetime_string, "%Y-%m-%d %H:%M")
        return True  
    except ValueError:
        return False  
def validate_start_and_end_times(starttime, endtime):
    """Validate that the end time is after the start time, returns a boolean result."""
    start_dt = datetime.strptime(starttime, "%Y-%m-%d %H:%M")
    end_dt = datetime.strptime(endtime, "%Y-%m-%d %H:%M")
    print(f"Parsed Start Time: {start_dt}, Parsed End Time: {end_dt}")
    if end_dt <= start_dt:
        return False  
    return True
def check_duplicates(participants_input):
    """Verify if a person was added more than once as a participant at a meeting."""
    participants = [p.strip() for p in participants_input.split(",")]
    seen=set()
    for name in participants:
        if name not in seen:
            seen.add(name)
        else:
            return True
    return False

def validate_participants(participants_input):
    """
    Validate that the participants' input is a comma-separated list of valid names.
    Each name must have at least two parts: Firstname and Lastname.
    
    Args:
        participants_input (str): A comma-separated string of participant names.

    Returns:
        bool: True if all names are valid, False otherwise.
    """
    # Regular expression to match a single valid name part (e.g., "John" or "Doe")
    name_pattern = r"^[A-Za-z]+(?:[-][A-Za-z]+)*$"  # Allows letters and optional hyphen

    # Split the input into individual participants
    participants = [p.strip() for p in participants_input.split(",")]

    # Validate each participant
    for name in participants:
        # Split each name into parts (first name, last name, etc.)
        name_parts = name.split()
        
        # Check if the name has at least two parts (Firstname and Lastname)
        if len(name_parts) < 2:
            return False  # Invalid: not enough parts
        
        # Check each part of the name against the regular expression
        for part in name_parts:
            if not re.match(name_pattern, part):
                return False  # Invalid: contains invalid characters

    # If all names pass validation
    return True

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
    
def add_meeting_gui():
    """Add a meeting to the database after validating the inputs: length less than 100 characters for title; valid time-format for start_time and end_time (YYYY-MM-DD HH:MM); valid list of participants (firstname lastname , fn2 ln2, ..)."""
    def save_meeting():
        meeting_title=meeting_title_entry.get()
        meeting_start_time=meeting_start_time_entry.get()
        meeting_end_time=meeting_end_time_entry.get()
        meeting_participants=meeting_participants_entry.get()
        if not meeting_title or not meeting_end_time or not meeting_start_time or not meeting_participants:
            messagebox.showerror("Error","Please complete all the fields in order to add a new meeting.")
            return
        if len(meeting_title)> 100:
            messagebox.showerror("Error","The meeting title must be shorter than 100 characters.")
            return
        if not validate_datetime(meeting_start_time):
            messagebox.showerror("Error","The start date or the time is not valid.")
            return    
        if not validate_datetime(meeting_end_time):
            messagebox.showerror("Error","The end date or the time is not valid.")
            return
        print(f"Start Time: {meeting_start_time}")
        print(f"End Time: {meeting_end_time}")
        meeting_start_time = meeting_start_time.strip()
        meeting_end_time = meeting_end_time.strip()


        if not validate_start_and_end_times(meeting_start_time,meeting_end_time):
            messagebox.showerror("Error","The end date (and time) should be after the start time (and time).")
            return
        if not validate_participants(meeting_participants):
            messagebox.showerror("Error","Invalid participation list")
            return  
        if  check_duplicates(meeting_participants):
            messagebox.showerror("Error","Invalid participation list (a person was added more than once)")
            return  
        try:
        
            meeting_title_entry.delete(0,"end")
            meeting_start_time_entry.delete(0,"end")
            meeting_end_time_entry.delete(0,"end")
            meeting_participants_entry.delete(0,"end")
            add_meeting(meeting_title,meeting_start_time,meeting_end_time, meeting_participants)
            messagebox.showinfo("Success",f"The meeting has been added.")
        except Exception as e:
            messagebox.showerror("Error",f"An error ocurred: {e}")
    window=Toplevel()
    window.geometry("600x500")
    window.title("Add meeting")
    title_label=Label(window,text="Add meeting",font=("Helvetica", 25))
    title_label.pack(pady=20)
    Label(window,text="Title:",font=("Helvetica", 15)).pack(pady=5)
    meeting_title_entry=Entry(window,width=30)
    meeting_title_entry.pack(pady=10)
    Label(window, text="Date and starting hour (YYYY-MM-DD HH:MM):", font=("Helvetica", 15)).pack(pady=5)
    meeting_start_time_entry=Entry(window,width=30)
    meeting_start_time_entry.pack(pady=10)
    Label(window, text="Date and ending hour (YYYY-MM-DD HH:MM):", font=("Helvetica", 15)).pack(pady=5)
    meeting_end_time_entry=Entry(window,width=30)
    meeting_end_time_entry.pack(pady=10)
    Label (window,text="Participants (firstname lastname , ...)", font=("Helvetica", 15)).pack(pady=5)
    meeting_participants_entry=Entry(window,width=30)
    meeting_participants_entry.pack(pady=10)
    Button(window,text="Save",command=save_meeting, font=("Helvetica", 10, "bold"), 
    width=10,                                           
    bg="lightblue",                 
    fg="black").pack(pady=10)