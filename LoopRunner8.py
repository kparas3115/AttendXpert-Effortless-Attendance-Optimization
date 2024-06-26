import tkinter as tk
from tkinter import filedialog
import pymysql.cursors
import pandas as pd
from pandasgui import show

class LoopRunner8(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Loop Runner")
        self.geometry("650x500")

        self.roll_count = 24  # Start at roll number 24
        self.total_rolls_from_db = 0
        self.i = 1

        self.roll_label = tk.Label(self, text=str(self.roll_count), font=("Tahoma", 68, "bold"))
        self.roll_label.place(x=300, y=100)

        self.present_button = tk.Button(self, text="Present", bg="green", width=10, command=self.present_action)
        self.present_button.place(x=50, y=380)

        self.absent_button = tk.Button(self, text="Absent", bg="red", width=10, command=self.absent_action)
        self.absent_button.place(x=200, y=380)

        self.excel_button = tk.Button(self, text="Attach Excel Sheet", width=15, command=self.attach_excel)
        self.excel_button.place(x=350, y=380)

        self.view_button = tk.Button(self, text="View Existing", width=15, command=self.view_existing)
        self.view_button.place(x=500, y=380)

        self.backward_button = tk.Button(self, text="<< Backward", width=15, command=self.backward)
        self.backward_button.place(x=200, y=420)

        self.forward_button = tk.Button(self, text="Forward >>", width=15, command=self.forward)
        self.forward_button.place(x=350, y=420)

    def present_action(self):
        if self.roll_count <= 46:  # End at roll number 46
            self.roll_count += 1
            self.roll_label.config(text=str(self.roll_count))

            try:
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='kps@3115',
                                             database='colmonsys',
                                             cursorclass=pymysql.cursors.DictCursor)

                with connection:
                    with connection.cursor() as cursor:
                        sql = "UPDATE stud_details SET em3 = em3 + 1 WHERE rollno = %s"
                        cursor.execute(sql, (self.roll_count,))
                        connection.commit()

            except pymysql.Error as e:
                print("Error:", e)

    def absent_action(self):
        if self.roll_count <= 46:  # End at roll number 46
            self.roll_count += 1
            self.roll_label.config(text=str(self.roll_count))

    def attach_excel(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            print("Selected Excel file:", file_path)
            # Read Excel file using pandas
            self.df = pd.read_excel(file_path)

    def view_existing(self):
        if hasattr(self, 'df'):
            show(self.df)  # Display DataFrame using pandasgui
        else:
            print("No Excel sheet attached yet.")

    def backward(self):
        if self.roll_count > 24:  # Start at roll number 24
            self.roll_count -= 1
            self.roll_label.config(text=str(self.roll_count))

    def forward(self):
        if self.roll_count <= 45:  # End at roll number 45
            self.roll_count += 1
            self.roll_label.config(text=str(self.roll_count))

if __name__ == "__main__":
    app = LoopRunner8()
    app.mainloop()
