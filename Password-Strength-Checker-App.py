from tkinter import *

def check_strength():
    password = password_entry.get()
    length = len(password)

    if length < 6:
        strength = "Weak"
    elif length < 10:
        strength = "Medium"
    else:
        strength = "Strong"

    result_label.config(text=f"Password Strength: {strength}")

root = Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

Label(root, text="Enter Password").pack(pady=10)

password_entry = Entry(root, show="*")
password_entry.pack()

Button(root, text="Check Strength", command=check_strength).pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()