from tkinter import *
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birth_date = date(year, month, day)
        today = date.today()

        age = today.year - birth_date.year

        # Check if birthday has occurred this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Present Age: {age} years")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date.")

# Create main window
root = Tk()
root.title("Age Calculator")
root.geometry("300x250")

# Labels and Entry widgets
Label(root, text="Enter Date of Birth").pack(pady=10)

Label(root, text="Day").pack()
day_entry = Entry(root)
day_entry.pack()

Label(root, text="Month").pack()
month_entry = Entry(root)
month_entry.pack()

Label(root, text="Year").pack()
year_entry = Entry(root)
year_entry.pack()

# Button
Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

# Result Label
result_label = Label(root, text="")
result_label.pack()

# Run application
root.mainloop()