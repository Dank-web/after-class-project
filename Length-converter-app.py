import tkinter as tk
from tkinter import messagebox

#Function to convert inches to centimeters
def convert():
    try:
        inches = float(entry_inches.get())
        centimeters = inches * 2.54
        result_label.config(
            text=f"{centimeters:.2f} cm",
            fg="#2E8B57"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enetr a valid number!")

# Main window
root = tk.Tk()
root.title("🌟 Inches to Centimeter Coverter")
root.geometry("450x300")
root.configure(bg="#E6F7FF")  #Light blue background
root.resizable(False, False)

#Title
title_label = tk.Label(
    root,
    text="📏 Length Converter",
    font=("Helvetica", 20, "bold"),
    bg="#E6F7FF",
    fg="#003366"
)
title_label.pack(pady=15)

# Input Frame
frame = tk.Frame(root, bg="#E6F7FF")
frame.pack(pady=10)

input_label = tk.Label(
    frame,
    text="Enter Length (inches):",
    font=("Arial", 12, "bold"),
    bg="#E6F7FF",
    fg="#333333"
)
input_label.grid(row=0, column=0, padx=5)

entry_inches = tk.Entry(
    frame,
    font=("Arial", 12),
    width=15,
    bd=3,
    relief="groove"
)
entry_inches.grid(row=0, column=1, padx=5)

# Convert Button
convert_btn = tk.Button(
    root,
    text="🔄 Convert",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45A049",
    activeforeground="white",
    padx=15,
    pady=5,
    command=convert,
    cursor="hand2"
)
convert_btn.pack(pady=15)

# Result Frame
result_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="ridge"
)
result_frame.pack(pady=10, padx=30, fill="x")

result_label = tk.Label(
    result_frame,
    text="Result will appear here",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="#003366",
    pady=10
)
result_label.pack()

# Footer
footer = tk.Label(
    root,
    text="✨ Tkinter Length Conversion App ✨",
    font=("Arial", 10, "italic"),
    bg="#E6F7FF",
    fg="#666666"
)
footer.pack(side="bottom", pady=10)

root.mainloop()