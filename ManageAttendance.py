import tkinter as tk
from LoopRunner16 import LoopRunner16
from LoopRunner17 import LoopRunner17
from LoopRunner18 import LoopRunner18
from LoopRunner19 import LoopRunner19
from LoopRunner20 import LoopRunner20

class ManageAttendance(tk.Tk):
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
        # Replace 'loopRunner()' with the appropriate code to manage attendance for EM3
        print("Opening Manage Attendance For EM3")
        LoopRunner16()

    def open_dsgt(self):
        # Replace 'loopRunner2()' with the appropriate code to manage attendance for DSGT
        print("Opening Manage Attendance For DSGT")
        LoopRunner17()

    def open_ds(self):
        # Replace 'loopRunner3()' with the appropriate code to manage attendance for DS
        print("Opening Manage Attendance For DS")
        LoopRunner18()

    def open_dlcoa(self):
        # Replace 'loopRunner4()' with the appropriate code to manage attendance for DLCOA
        print("Opening Manage Attendance For DLCOA")
        LoopRunner19()

    def open_cg(self):
        # Replace 'loopRunner5()' with the appropriate code to manage attendance for CG
        print("Opening Manage Attendance For CG")
        LoopRunner20()

if __name__ == "__main__":
    app = ManageAttendance()
    app.mainloop()
