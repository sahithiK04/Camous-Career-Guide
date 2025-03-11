import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

# Sample student credentials (replace with your own authentication logic)
valid_credentials = {"username": "123", "password": "123"}

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")

def center_window_toplevel(root, toplevel):
    toplevel.update_idletasks()
    width = toplevel.winfo_width()
    height = toplevel.winfo_height()
    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 2
    toplevel.geometry(f"{width}x{height}+{x}+{y}")

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
    second_window.geometry("600x400")
    center_window_toplevel(root, second_window)

    
    bg_image = Image.open(r"C:\Users\HEMASRI\Downloads\college.jpeg")
    bg_photo = ImageTk.PhotoImage(bg_image.resize((600, 600)))  # Resize the image
    background_label = tk.Label(second_window, image=bg_photo)
    background_label.image = bg_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

 
    listbox = tk.Listbox(second_window, font=("Helvetica", 18))  # Set font size to 16
    for company in company_names:
        listbox.insert(tk.END, company)
    listbox.pack()


    # Submit button in the second page
    submit_button = tk.Button(second_window, text="Submit", font=("Helvetica", 16), command=lambda: display_company_data(listbox.get(tk.ACTIVE)))
    submit_button.pack()

def display_company_data(company_name):
    conn = sqlite3.connect('company.db')
    c = conn.cursor()

    
    c.execute("SELECT * FROM StudentPro WHERE Company=?", (company_name,))
    data = c.fetchall()

    conn.close()

    
    display_window = tk.Toplevel()
    display_window.title(f"{company_name} Employees")
    display_window.geometry("600x400")
    center_window_toplevel(root, display_window)

    
    bg_image = Image.open(r"C:\Users\HEMASRI\Downloads\college.jpeg")
    bg_photo = ImageTk.PhotoImage(bg_image.resize((500, 500)))  
    background_label = tk.Label(display_window, image=bg_photo)
    background_label.image = bg_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    

    text_widget = tk.Text(display_window)
    for row in data:
        text_widget.insert(tk.END, f"ID: {row[0]}\n")
        text_widget.insert(tk.END, f"Name:{row[1]}\n")
        text_widget.insert(tk.END, f"Email:{row[2]}\n")
        text_widget.insert(tk.END, f"Company:{row[3]}\n")
        text_widget.insert(tk.END, f"Position:{row[4]}\n")
        text_widget.insert(tk.END, f"Phno:{row[5]}\n\n")
    text_widget.pack()

# Front page
front_page = tk.Tk()
title_label = tk.Label(front_page, text="CAMPUS CAREER GUIDE", font=("Helvetica", 40))
title_label.place(x=200,y=700)

# Set the size of the window and center it
front_page_width = 500
front_page_height = 500
center_window(front_page, front_page_width, front_page_height)


bg_image = Image.open(r"C:\Users\HEMASRI\Downloads\college.jpeg")
bg_photo = ImageTk.PhotoImage(bg_image.resize((500, 500)))  # Resize the image
background_label = tk.Label(front_page, image=bg_photo)
background_label.image = bg_photo
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Heading
heading_label = tk.Label(front_page, text="CAMPUS CAREER GUIDE", font=("Helvetica", 28))
heading_label.pack(pady=20)

# Enter button to proceed to login
enter_button = tk.Button(front_page, text="ENTER", command=front_page.destroy, font=("Helvetica", 16))
enter_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# Sample company names (replace with your own data)
company_names = ["Microsoft", "Flipkart", "Amazon", "Google"]

front_page.mainloop()

# Now, the main application window (root) will be opened after closing the front page
root = tk.Tk()
root.title("Student Login")

# Set the size of the window and center it
window_width = 500
window_height = 500
center_window(root, window_width, window_height)

# Load background image
bg_image = Image.open(r"C:\Users\HEMASRI\Downloads\college.jpeg")
bg_photo = ImageTk.PhotoImage(bg_image.resize((window_width, window_height)))  # Resize the image
background_label = tk.Label(root, image=bg_photo)
background_label.image = bg_photo
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# create and place login form widgets
frame = tk.Frame(root)
frame.pack(padx=80, pady=80)

username_label = tk.Label(frame, text="Username:", font=("Helvetica", 15), padx=8, pady=8)
username_label.pack()

# Create and place username entry with larger font size
username_entry = tk.Entry(frame, font=("Helvetica", 11))
username_entry.pack()


password_label = tk.Label(frame, text="Passwords:",font=("Helvetica", 15), padx=8, pady=8)
password_label.pack()

password_entry = tk.Entry(frame, show="*", font=("Helvetica", 11))  
password_entry.pack()

login_button = tk.Button(root, text="Login",font=("Helvetica", 13), padx=8, pady=8, command=login)
login_button.pack()

root.mainloop()
