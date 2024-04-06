import tkinter as tk

class LabBatches(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Lab Batches")

        self.B1_button = tk.Button(self, text="Batch B1", command=self.open_managelab)
        self.B1_button.place(x=50, y=20, width=300, height=50)

        self.B2_button = tk.Button(self, text="Batch B2", command=self.open_managelab)
        self.B2_button.place(x=50, y=100, width=300, height=50)

        self.B3_button = tk.Button(self, text="Batch B3", command=self.open_managelab)
        self.B3_button.place(x=50, y=180, width=300, height=50)

        # Add background image if needed
        # self.background_image = tk.PhotoImage(file="images/bg.jpg")
        # self.background_label = tk.Label(self, image=self.background_image)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def open_managelab(self):
        # Replace 'managelab()' with the appropriate code to manage the corresponding lab batch
        print("Opening Manage Lab for selected batch")

if __name__ == "__main__":
    app = LabBatches()
    app.mainloop()
