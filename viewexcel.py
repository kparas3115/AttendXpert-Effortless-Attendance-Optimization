import tkinter as tk
import os
import win32com.client as win32
from datetime import datetime

class ViewExcel:
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

        self.last_updated_label = tk.Label(self.master, text="Last Updated:")
        self.last_updated_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.last_updated_var = tk.StringVar()
        self.last_updated_var.set("")
        self.last_updated_value = tk.Label(self.master, textvariable=self.last_updated_var)
        self.last_updated_value.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.view_button = tk.Button(self.master, text="View Excel", command=self.view_excel)
        self.view_button.grid(row=3, column=0, padx=5, pady=5, sticky=tk.EW)

        self.open_button = tk.Button(self.master, text="Open Selected", command=self.open_selected)
        self.open_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)

        self.update_file_list()

    def update_file_list(self):
        directory = 'C:\\Users\paras\OneDrive\डेस्कटॉप\Excel Files'
        self.file_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
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
            file_path = os.path.join('C:\\Users\paras\OneDrive\डेस्कटॉप\Excel Files', selected_file)
            os.startfile(file_path)  # Open the selected file with its associated program

    def view_excel(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_file = self.filtered_files[selected_index[0]]
            file_path = os.path.join('C:\\Users\paras\OneDrive\डेस्कटॉप\Excel Files', selected_file)

            # Get last modified time of the file
            last_modified_timestamp = os.path.getmtime(file_path)
            last_modified_time = datetime.fromtimestamp(last_modified_timestamp)

            # Display last modified time
            self.last_updated_var.set(last_modified_time.strftime("%Y-%m-%d %H:%M:%S"))

            excel = win32.Dispatch("Excel.Application")
            excel.Visible = True
            workbook = excel.Workbooks.Open(file_path, ReadOnly=True)  # Open the selected file in read-only mode

def main():
    root = tk.Tk()
    app = ViewExcel(root)
    root.mainloop()

if __name__ == "__main__":
    main()

