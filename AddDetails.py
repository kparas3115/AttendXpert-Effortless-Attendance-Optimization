import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import sqlite3

class AddDetails(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("600x700")
        self.title("Add Details")

        self.font = ("Tahoma", 14, "bold")
        self.x = 80
        self.txtX = 250
        self.txtWidth = 200
        self.txtHeight = 40

        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self, text="Name", font=self.font).place(x=self.x, y=70)
        tk.Label(self, text="D.O.B", font=self.font).place(x=self.x, y=190)
        tk.Label(self, text="Gender", font=self.font).place(x=self.x, y=250)
        tk.Label(self, text="Address", font=self.font).place(x=self.x, y=310)
        tk.Label(self, text="Contact", font=self.font).place(x=self.x, y=370)
        tk.Label(self, text="Blood Group", font=self.font).place(x=self.x, y=430)
        tk.Label(self, text="Batch", font=self.font).place(x=self.x, y=490)

        # Entry widgets
        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.place(x=self.txtX, y=70)

        self.address_entry = tk.Entry(self, width=30)
        self.address_entry.place(x=self.txtX, y=310)

        self.contact_entry = tk.Entry(self, width=30)
        self.contact_entry.place(x=self.txtX, y=370)

        # Date of Birth widget
        self.dob_entry = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.dob_entry.place(x=self.txtX, y=190)

        # Gender radio buttons
        self.gender_var = tk.StringVar(value="Male")
        tk.Radiobutton(self, text="Male", variable=self.gender_var, value="Male").place(x=self.txtX, y=250)
        tk.Radiobutton(self, text="Female", variable=self.gender_var, value="Female").place(x=self.txtX + 120, y=250)

        # Blood Group and Batch dropdowns
        self.blood_group_combo = ttk.Combobox(self, values=["Select", "A+", "A-", "B+", "B-", "AB+", "O+", "O-"])
        self.blood_group_combo.place(x=self.txtX, y=430)
        self.blood_group_combo.current(0)

        self.batch_combo = ttk.Combobox(self, values=["B1", "B2", "B3"])
        self.batch_combo.place(x=self.txtX, y=490)
        self.batch_combo.current(0)

        # Add Data Button
        self.add_data_btn = tk.Button(self, text="Add Data", command=self.add_data)
        self.add_data_btn.place(x=400, y=610)

    def add_data(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()
        dob = self.dob_entry.get()
        gender = self.gender_var.get()
        blood_group = self.blood_group_combo.get()
        batch = self.batch_combo.get()

        # Connect to database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Insert data into database
        try:
            cursor.execute("INSERT INTO stud_details (name, gender, address, contact, batch, dob, bldGrp) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (name, gender, address, contact, batch, dob, blood_group))
            conn.commit()
            messagebox.showinfo("Success", "Data Added Successfully")
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Failed to Add Data")

        conn.close()

if __name__ == "__main__":
    app = AddDetails()
    app.mainloop()




# djwaj