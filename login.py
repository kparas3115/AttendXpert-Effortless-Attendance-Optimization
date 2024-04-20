import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess
class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("600x400")

        self.f1 = ("Tahoma", 20, "bold")

        l1 = tk.Label(self, text="Username", font=self.f1)
        l1.place(x=100, y=80)

        l2 = tk.Label(self, text="Password", font=self.f1)
        l2.place(x=100, y=160)

        self.username = tk.Entry(self, font=self.f1)
        self.username.place(x=250, y=80, width=150)

        self.password = tk.Entry(self, font=self.f1, show="*")
        self.password.place(x=250, y=160, width=150)

        self.signin = tk.Button(self, text="Sign In", font=self.f1, command=self.authenticate)
        self.signin.place(x=200, y=260, width=120, height=50)

        self.cancel = tk.Button(self, text="Cancel", font=self.f1, command=self.destroy)
        self.cancel.place(x=400, y=260, width=120, height=50)

    def authenticate(self):
        username = self.username.get()
        password = self.password.get()

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='kps@3115',
                database='colmonsys'
            )
            c = conn.cursor()

            c.execute("SELECT * FROM login WHERE username=%s AND password=%s", (username, password))
            row = c.fetchone()

            if row:
                messagebox.showinfo("Login Successful", "Login Successful")
                self.destroy()  # Close login window
                AssistantOpener()  # Open assistantopener window
            else:
                messagebox.showerror("Invalid Credentials", "Invalid Login Credentials")

            conn.close()
        except mysql.connector.Error as e:
            print(e)

class AssistantOpener(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Assistant Opener")
        self.geometry("300x200")

        self.activate_button = tk.Button(self, text="Activate AttendXpert", font=("Tahoma", 12), command=self.activate_attendxpert)
        self.activate_button.place(relx=0.5, rely=0.5, anchor="center")

    def activate_attendxpert(self):
        # Add your code here to activate AttendXpert (AMS AI)
       print('AttendXpert Activated!')


if __name__ == "__main__":
    login = Login()
    login.mainloop()
