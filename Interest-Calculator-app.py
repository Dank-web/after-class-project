from tkinter import *

def calculate():
    p = float(principal_entry.get())
    t = float(time_entry.get())
    r = float(rate_entry.get())

    # Simple Interest
    si = (p * r * t) / 100

    # Compound Interest
    ci = p * ((1 + r / 100) ** t) - p

    result_label.config(
        text=f"Simple Interest = {si:.2f}\nCompound Interest = {ci:.2f}"
    )

root = Tk()
root.title("Interest Calculator")
root.geometry("350x250")

Label(root, text="Principal Amount").pack()
principal_entry = Entry(root)
principal_entry.pack()

Label(root, text="Time Period (Years)").pack()
time_entry = Entry(root)
time_entry.pack()

Label(root, text="Rate of Interest (%)").pack()
rate_entry = Entry(root)
rate_entry.pack()

Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()