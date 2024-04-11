import tkinter as tk

from LoopRunner import LoopRunner
from LoopRunner2 import LoopRunner2
from LoopRunner3 import LoopRunner3
from LoopRunner4 import LoopRunner4
from LoopRunner5 import LoopRunner5


class ManageLab(tk.Tk):
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
        LoopRunner()

    def open_dsgt(self):
        print("Opening Manage Attendance For DSGT")
        LoopRunner2()

    def open_ds(self):
        print("Opening Manage Attendance For DS")
        LoopRunner3()

    def open_dlcoa(self):
        print("Opening Manage Attendance For DLCOA")
        LoopRunner5()
    def open_cg(self):
        print("Opening Manage Attendance For CG")
        LoopRunner4()

if __name__ == "__main__":
    app = ManageLab()
    app.mainloop()

