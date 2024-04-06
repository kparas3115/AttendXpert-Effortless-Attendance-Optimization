import tkinter as tk
from tkinter import ttk
import PIL.Image as Image
import PIL.ImageTk as ImageTk

class Starter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")

        self.frame = ttk.Frame(self)
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        image = Image.open("images/AMS.jpg")
        image = image.resize((1280, 720))
        self.photo = ImageTk.PhotoImage(image)
        self.background_label = ttk.Label(self.frame, image=self.photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.login_button = ttk.Button(self.frame, text="LOGIN", command=self.on_login, style="Transparent.TButton", name="login")
        self.login_button.place(relx=0.85, rely=0.83, width=100, height=30)

    def on_login(self):
        login = Login()
        self.withdraw()

class Login(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("Login")

        # Add your login widgets here
        # For example:
        # self.username_label = ttk.Label(self, text="Username:")
        # self.username_label.pack()
        # self.username_entry = ttk.Entry(self)
        # self.username_entry.pack()
        # self.password_label = ttk.Label(self, text="Password:")
        # self.password_label.pack()
        # self.password_entry = ttk.Entry(self, show="*")
        # self.password_entry.pack()
        # self.login_button = ttk.Button(self, text="Login", command=self.login)
        # self.login_button.pack()

if __name__ == "__main__":
    app = Starter()
    app.mainloop()
