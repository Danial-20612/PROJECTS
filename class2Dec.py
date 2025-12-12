import tkinter as tk
from tkinter import messagebox

# def hello():
#     print("Good morning: ")
# def bye():
#     print("Bye see you later: ")
 
root = tk.Tk()
# root.title("Bro Code")
# root.minsize(300,150)

# greeting_label = tk.Label(root, text="Click the button to see greetings: ")
# greet_button = tk.Button(root, text="Click me" , command=hello)

# bye_label = tk.Label(root, text="Click here the button to see Bye message")
# bye_button = tk.Button(root, text="Click me" , command=bye )

# greeting_label.pack(pady=10)
# greet_button.pack(pady=10)
# bye_button.pack(pady=10)
# bye_label.pack(pady=10)

# root.mainloop()

#-------------------------------------------------------------------------------
## log in system ##
# def login():
#     username = username_entry.get()
#     password = password_entry.get()

#     if username == "" or password == "":
#         messagebox.showerror("Error both fields required")
#     elif username == "admin" and password == "1234":
#         messagebox.showinfo("Success, login sucessful")
#     else:
#         messagebox.showwarning("Warning, Incorrect details")

# username_label = tk.Label(root, text="Username: ")
# username_label.pack(pady= (10,0))
# username_entry = tk.Entry(root)
# username_entry.pack(pady=5)

# password_label = tk.Label(root, text="Password: ")
# password_label.pack(pady=(10,0))
# password_entry = tk.Entry(root, show="*")
# password_entry.pack(pady=5)

# login_button = tk.Button(root, text="Login" , command=login)
# login_button.pack(pady=10)

# root.mainloop()

root.geometry("500x200")

# Standard Button with custom colors
btn1 = tk.Button(
    root, 
    text="Click Me", 
    bg="Purple",               # Background color
    fg="white",                # Text color
    activebackground="red",    # Color when clicked
    activeforeground="white",  # Text color when clicked
    font=("Arial", 25)
)

btn2 = tk.Button(
    root,
    text="Click Me",
    bg="Green",
    fg="lightgreen",
    activebackground="yellow",
    activeforeground="black",
    font=("Arial", 25)
)

btn1.pack(pady=20)
btn2.pack(pady=0)
root.mainloop()