import tkinter as tk
from LoopRunner11 import LoopRunner11
from LoopRunner12 import LoopRunner12
from LoopRunner13 import LoopRunner13
from LoopRunner14 import LoopRunner14
from LoopRunner15 import LoopRunner15

class ManageLab3(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Manage Attendance")

        self.em3_button = tk.Button(self, text="Manage Attendance For EM3", command=self.open_em3)
        self.em3_button.place(x=50, y=20, width=300, height=20)

        self.dsgt_button = tk.Button(self, text="Manage Attendance For DSGT", command=self.open_dsgt)
        self.dsgt_button.place(x=50, y=60, width=300, height=20)

        self.ds_button = tk.Button(self, text="Manage Attendance For DS", command=self.open_ds)
        self.ds_button.place(x=50, y=100, width=300, height=20)

        self.dlcoa_button = tk.Button(self, text="Manage Attendance For DLCOA", command=self.open_dlcoa)
        self.dlcoa_button.place(x=50, y=140, width=300, height=20)

        self.cg_button = tk.Button(self, text="Manage Attendance For CG", command=self.open_cg)
        self.cg_button.place(x=50, y=180, width=300, height=20)

        def open_em3(self):
            print("Opening Manage Attendance For EM3")
            LoopRunner11()

        def open_dsgt(self):
            print("Opening Manage Attendance For DSGT")
            LoopRunner12()

    def open_ds(self):
        print("Opening Manage Attendance For DS")
        LoopRunner13()

    def open_dlcoa(self):
        print("Opening Manage Attendance For DLCOA")
        LoopRunner14()

    def open_cg(self):
        print("Opening Manage Attendance For CG")
        LoopRunner15()

if __name__ == "__main__":
    app = ManageLab3()
    app.mainloop()

