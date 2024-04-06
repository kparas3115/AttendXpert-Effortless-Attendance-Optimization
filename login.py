import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")

        self.title("Login")

        self.username_label = ttk.Label(self, text="Username", font=("Tahoma", 20, "bold"))
        self.username_label.place(x=100, y=80)

        self.password_label = ttk.Label(self, text="Password", font=("Tahoma", 20, "bold"))
        self.password_label.place(x=100, y=160)

        self.username_entry = ttk.Entry(self, font=("Tahoma", 20))
        self.username_entry.place(x=250, y=80, width=150)

        self.password_entry = ttk.Entry(self, show="*", font=("Tahoma", 20))
        self.password_entry.place(x=250, y=160, width=150)

        self.signin_button = ttk.Button(self, text="Sign In", command=self.signin, style="TButton")
        self.signin_button.place(x=200, y=260, width=120, height=50)

        self.cancel_button = ttk.Button(self, text="Cancel", command=self.cancel, style="TButton")
        self.cancel_button.place(x=400, y=260, width=120, height=50)

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Tahoma", 20))

    def signin(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            conn = sqlite3.connect('your_database.db')
            c = conn.cursor()
            c.execute("SELECT * FROM login WHERE username = ? AND password = ?", (username, password))
            result = c.fetchone()

            if result:
                messagebox.showinfo("Success", "Login Successful")
                self.destroy()
                dashboard = Dashboard()
                dashboard.mainloop()
            else:
                messagebox.showerror("Error", "Invalid Login Credentials")

            conn.close()
        except Exception as e:
            print(e)

    def cancel(self):
        self.destroy()

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Dashboard")

        # Add your dashboard widgets here

if __name__ == "__main__":
    login = Login()
    login.mainloop()
