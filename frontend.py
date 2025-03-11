import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

# Sample company names (replace with your own data)
company_names = ["Meesho", "Flipkart", "Amazon", "NXP"]

# Sample student credentials (replace with your own authentication logic)
valid_credentials = {"username": "123", "password": "123"}

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")

def enter_main_page():
    entry_root.withdraw()  # Hide the entry page
    root.deiconify()

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == valid_credentials["username"] and entered_password == valid_credentials["password"]:
        messagebox.showinfo("Login Successful", "Welcome student!")
        open_second_page()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

def open_second_page():
    root.withdraw()  # Hide the login page
    second_window = tk.Toplevel(root)
    second_window.title("Company Names")
    center_window(root, 400, 400)

    # Create a Listbox to display company names
    listbox = tk.Listbox(second_window)
    for company in company_names:
        listbox.insert(tk.END, company)
    listbox.pack()

    # Submit button in the second page
    submit_button = tk.Button(second_window, text="Submit", command=lambda: display_company_data(listbox.get(tk.ACTIVE)))
    submit_button.pack()

def display_company_data(company_name):
    conn = sqlite3.connect('company.db')
    c = conn.cursor()

    # Fetch data for the selected company
    c.execute("SELECT * FROM StudentPro WHERE Company=?", (company_name,))
    data = c.fetchall()

    conn.close()

    # Display the data in a new window
    display_window = tk.Toplevel()
    display_window.title(f"{company_name} Employees")
    center_window(root, 100, 100)

    text_widget = tk.Text(display_window)
    for row in data:
        text_widget.insert(tk.END, f"ID: {row[0]}\n")
        text_widget.insert(tk.END, f"Name: {row[1]}\n")
        text_widget.insert(tk.END, f"Email: {row[2]}\n")
        text_widget.insert(tk.END, f"Company: {row[3]}\n")
        text_widget.insert(tk.END, f"Position: {row[4]}\n")
        text_widget.insert(tk.END, f"Phno: {row[5]}\n\n")
    text_widget.pack()

entry_root = tk.Tk()
entry_root.title("Campus Entry Page")
center_window(entry_root, 400, 200)

heading_label = tk.Label(entry_root, text="Campus Career Guide", font=("Arial", 24, "bold"))
heading_label.pack(pady=30)

enter_button = tk.Button(entry_root, text="Enter", font=("Arial", 16), command=enter_main_page)
enter_button.pack(pady=30)

# Login page
root = tk.Toplevel(entry_root)
root.title("Student Login")
root.withdraw()  # Hide the login page initially



# create and place login form widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)



username_label = tk.Label(frame, text="Username:")
username_label.pack()

username_entry = tk.Entry(frame)
username_entry.pack()

password_label = tk.Label(frame, text="Passwords:")
password_label.pack()

password_entry = tk.Entry(frame, show="*")  # mask the password
password_entry.pack()

login_button = tk.Button(frame, text="Login", command=login)
login_button.pack()

entry_root.mainloop()
