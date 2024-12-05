from tkinter import *
from tkinter import ttk  # Import ttk for Combobox

# Create the main window
root = Tk()
root.title("Registration Form")
root.geometry("500x400")
root.configure(bg="#333")  # Set a light blue background color

# Function to handle form submission
def submit_value():
    print("Your information has been saved successfully")

# Title Label
Label(
    root,
    text="Python Registration Form",
    font="Helvetica 18 bold",
    bg="#333",
    fg="white"
).grid(row=0, column=1, columnspan=2, pady=20)

# Form Labels
Label(root, text="Full Name", font="Arial 12", bg="#333",fg="white").grid(row=1, column=0, sticky="e", padx=10, pady=5)
Label(root, text="Branch", font="Arial 12", bg="#333",fg="white").grid(row=2, column=0, sticky="e", padx=10, pady=5)
Label(root, text="Gender", font="Arial 12", bg="#333",fg="white").grid(row=3, column=0, sticky="e", padx=10, pady=5)
Label(root, text="Age", font="Arial 12", bg="#333",fg="white").grid(row=4, column=0, sticky="e", padx=10, pady=5)
Label(root, text="Contact No", font="Arial 12", bg="#333",fg="white").grid(row=5, column=0, sticky="e", padx=10, pady=5)
Label(root, text="Email", font="Arial 12", bg="#333",fg="white").grid(row=6, column=0, sticky="e", padx=10, pady=5)

# Variables to store form values
name_value = StringVar()
branch_value = StringVar()
gender_value = StringVar()
age_value = StringVar()
phone_value = StringVar()
email_value = StringVar()
check_value = IntVar()

# Form Entry Fields
Entry(root, textvariable=name_value, font="Arial 12").grid(row=1, column=1, pady=5, padx=10)
Entry(root, textvariable=branch_value, font="Arial 12").grid(row=2, column=1, pady=5, padx=10)

# Gender Field as Combobox
gender_combobox = ttk.Combobox(
    root,text="Gender",
    textvariable=gender_value,
    font="Arial 12",
    state="readonly",width=18
)
gender_combobox['values'] = ("Female", "Male", "Other","Transgender")  # Predefined gender options
gender_combobox.grid(row=3, column=1, pady=5, padx=10)
gender_combobox.current(0)  # Set default value to the first option ("Female")

# Other Form Entry Fields
Entry(root, textvariable=age_value, font="Arial 12").grid(row=4, column=1, pady=5, padx=10)
Entry(root, textvariable=phone_value, font="Arial 12").grid(row=5, column=1, pady=5, padx=10)
Entry(root, textvariable=email_value, font="Arial 12").grid(row=6, column=1, pady=5, padx=10)

# "Remember Me" Checkbox
Checkbutton(
    root, 
    text="Remember Me?", 
    variable=check_value, 
    font="Arial 10", 
    bg="#333",fg="white"
).grid(row=7, column=1, pady=10)

# Submit Button
Button(
    root, 
    text="Submit", 
    command=submit_value, 
    font="Arial 12 bold", 
    bg="#ff3399",
    fg="white", 
    padx=10, 
    pady=5
).grid(row=8, column=1, pady=20)

# Start the GUI event loop
root.mainloop()
