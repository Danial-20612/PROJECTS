import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
 
# --------------------------
# Conversion Function
# --------------------------
def convert():
    try:
        # Try converting input to float
        value = float(entry_value.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return
 
    conversion = combo.get()
 
    # Conversion logic
    if conversion == "Meters → Feet":
        result = value * 3.28084
    elif conversion == "Feet → Meters":
        result = value / 3.28084
 
    elif conversion == "Litres → Gallons":
        result = value * 0.219969
    elif conversion == "Gallons → Litres":
        result = value / 0.219969
 
    elif conversion == "Kilograms → Pounds":
        result = value * 2.20462
    elif conversion == "Pounds → Kilograms":
        result = value / 2.20462
 
    else:
        result = "Invalid selection"
 
    # Display the result
    label_result.config(text=f"Result: {result:.4f}")
 
 
# --------------------------
# GUI WINDOW
# --------------------------
root = tk.Tk()
root.title("Unit Converter")
root.geometry("350x250")
 
# --------------------------
# Widgets
# --------------------------
# Input label and box
tk.Label(root, text="Enter a value:", font=("Arial", 11)).pack(pady=5)
entry_value = tk.Entry(root, width=20, font=("Arial", 11))
entry_value.pack()
 
# Dropdown menu
tk.Label(root, text="Select a conversion:", font=("Arial", 11)).pack(pady=5)
 
options = [
    "Meters → Feet",
    "Feet → Meters",
    "Litres → Gallons",
    "Gallons → Litres",
    "Kilograms → Pounds",
    "Pounds → Kilograms"
]
 
combo = ttk.Combobox(root, values=options, width=25, state="readonly", font=("Arial", 10))
combo.current(0)
combo.pack()
 
# Convert button
btn_convert = tk.Button(root, text="Convert", font=("Arial", 11), command=convert)
btn_convert.pack(pady=15)
 
# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
label_result.pack(pady=10)
 
# --------------------------
# Main loop
# --------------------------
root.mainloop()