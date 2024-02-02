import Login
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import keyboard
import pandas as pd

def authen(usrname, password):
    df = pd.read_csv('D:/PyThon/SimpleGui/user.csv')
    return not df[(df['username'] == usrname) & (df['password'] == password)].empty
def check_login():
    username = entry_username.get()
    password = entry_password.get()

    # Replace this with your actual login logic
    if authen(username, password):
        # Close the login window
        app.withdraw()

        # Open the welcome window
        open_welcome_window(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_welcome_window(username):
    # Create a new window for welcome message
    welcome_window = tk.Toplevel()
    welcome_window.iconbitmap('D:/PyThon/SimpleGui/apple_1.ico')
    welcome_window.title("Welcome")

    # Display a welcome message
    welcome_label = ttk.Label(welcome_window, text="Welcome, {} \n Click buttons".format(username), font=("Helvetica", 20, 'bold'), justify='center')
    welcome_label.pack(padx=100, pady=50)

    # Add buttons A, B, C, D
    button_a = ttk.Button(welcome_window, text="vOffice", command=lambda: button_clicked("A"))
    button_b = ttk.Button(welcome_window, text="SapSf", command=lambda: button_clicked("B"))
    button_c = ttk.Button(welcome_window, text="vOps", command=lambda: button_clicked("C"))
    button_d = ttk.Button(welcome_window, text="Login VDI", command=lambda: button_clicked("D"))
    button_cancel = ttk.Button(welcome_window, text="Cancel", command=app.quit)

    button_a.pack(pady=20)
    button_b.pack(pady=20)
    button_c.pack(pady=20)
    button_d.pack(pady=20)
    button_cancel.pack(pady=20)

def button_clicked(button):
    if button == "A":
        webbrowser.open("voffice.viettel.vn/app-view/")
    elif button == "B":
        webbrowser.open("hcm44.sapsf.com")
    elif button == "C":
        webbrowser.open("vops.viettel.vn")
    elif button == "D":
        Login.OpenVMware().running()
    else:
        messagebox.showinfo("Button Clicked", "You clicked Button {}".format(button))

def save_user():
    f = open('D:/PyThon/SimpleGui/user.csv', 'a')
    un = entry_su_username.get()
    pw = entry_su_pw.get()
    f.write(un); f.write(","); f.write(pw); f.write("\n")
    messagebox.showinfo("Button Clicked", "Sign success, You can login now")

def sign_up():
    global signup_window
    signup_window = tk.Toplevel()
    signup_window.title("Sign Up")
    su_username = ttk.Label(signup_window, text="Username:")
    su_username.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    global entry_su_username
    entry_su_username = ttk.Entry(signup_window)
    entry_su_username.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    su_pw = ttk.Label(signup_window, text="Password:")
    su_pw.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    global entry_su_pw
    entry_su_pw = ttk.Entry(signup_window, show="*")
    entry_su_pw.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    save_button = ttk.Button(signup_window, text="Save", command=save_user)
    save_button.grid(row=2, column=0, pady=20)


# Creating main application window
app = tk.Tk()
app.title("Login App")
app.iconbitmap("D:/PyThon/SimpleGui/apple.ico")

# Creating and applying a style
style = ttk.Style()
style.configure("TLabel", padding=20)
style.configure("TButton", padding=10)

# Creating and placing widgets with updated style
label_username = ttk.Label(app, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_username = ttk.Entry(app)
entry_username.grid(row=0, column=1, padx=10, pady=5, sticky="w")

label_password = ttk.Label(app, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_password = ttk.Entry(app, show="❤️️")
entry_password.grid(row=1, column=1, padx=10, pady=5, sticky="w")

login_button = ttk.Button(app, text="Login", command=check_login)
login_button.grid(row=2, column=0, pady=20)

signup_button = ttk.Button(app, text="Signup", command=sign_up)
signup_button.grid(row=2, column=1, pady=20, sticky="w")

cancel_button = ttk.Button(app, text="Cancel", command=app.quit)
cancel_button.grid(row=2, column=2, pady=20, sticky="w")


# Start the application
app.mainloop()


