import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

class viewexcel:
    def __init__(self, master):
        self.master = master
        self.master.title("Excel File Viewer")

        self.file_list = []
        self.filtered_files = []

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.filter_files)

        self.search_label = tk.Label(self.master, text="Search:")
        self.search_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.search_entry = tk.Entry(self.master, textvariable=self.search_var)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        self.file_listbox = tk.Listbox(self.master, height=20)
        self.file_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW)

        self.scrollbar = tk.Scrollbar(self.master, orient="vertical", command=self.file_listbox.yview)
        self.scrollbar.grid(row=1, column=2, sticky="ns")
        self.file_listbox.config(yscrollcommand=self.scrollbar.set)

        self.view_button = tk.Button(self.master, text="View Excel", command=self.view_excel)
        self.view_button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.EW)

        self.open_button = tk.Button(self.master, text="Open Selected", command=self.open_selected)
        self.open_button.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

        self.update_file_list()
        self.timer()

    def update_file_list(self):
        directory = os.getcwd()  # Assuming the current working directory
        self.file_list = [f for f in os.listdir(directory) if f.endswith('.xlsx')]
        self.filtered_files = self.file_list[:]
        self.update_file_listbox()

    def update_file_listbox(self):
        self.file_listbox.delete(0, tk.END)
        for file in self.filtered_files:
            self.file_listbox.insert(tk.END, file)

    def filter_files(self, *args):
        query = self.search_var.get()
        self.filtered_files = [f for f in self.file_list if query.lower() in f.lower()]
        self.update_file_listbox()

    def open_selected(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_file = self.filtered_files[selected_index[0]]
            file_path = os.path.join(os.getcwd(), selected_file)
            df = pd.read_excel(file_path)
            print(df)  # You can replace this with your desired action with the dataframe

    def view_excel(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_file = self.filtered_files[selected_index[0]]
            file_path = os.path.join(os.getcwd(), selected_file)
            os.system(file_path)

    def timer(self):
        self.update_file_list()
        self.master.after(5000, self.timer)  # Update every 5 seconds


def main():
    root = tk.Tk()
    app = viewexcel(root)
    root.mainloop()


if __name__ == "__main__":
    main()
