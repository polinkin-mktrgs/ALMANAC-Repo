import tkinter as tk
from tkinter import ttk
import pandas as pd

class ExcelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Macxel")

        self.table = ttk.Treeview(self.root)
        self.table["columns"] = ("col1", "col2", "col3", "col4", "col5")
        self.table.heading("#0", text="Параметры")
        self.table.column("#0", width=100)
        self.table.heading("col1", text="1")
        self.table.column("col1", width=50)
        self.table.heading("col2", text="2")
        self.table.column("col2", width=50)
        self.table.heading("col3", text="3")
        self.table.column("col3", width=50)
        self.table.column("col4", width=50)
        self.table.heading("col4", text="4")
        self.table.column("col5", width=50)
        self.table.heading("col5", text="5")
        self.table.pack()
        self.table = ttk.Treeview(self.root)
        self.table["columns"] = ("col1", "col2", "col3", "col4", "col5")
        self.table.heading("#0", text="Параметры")
        self.table.column("#0", width=100)
        self.table.heading("col1", text="1")
        self.table.column("col1", width=50)
        self.table.heading("col2", text="2")
        self.table.column("col2", width=50)
        self.table.heading("col3", text="3")
        self.table.column("col3", width=50)
        self.table.column("col4", width=50)
        self.table.heading("col4", text="4")
        self.table.column("col5", width=50)
        self.table.heading("col5", text="5")
        self.table.pack()

        self.df = pd.DataFrame(columns=["col1", "col2", "col3"])

        self.add_row_button = ttk.Button(self.root, text="Add Row", command=self.add_row)
        self.add_row_button.pack()

    def add_row(self):
        row_data = {"col1": "Value 1", "col2": "Value 2", "col3": "Value 3"}
        self.df = self.df.append(row_data, ignore_index=True)
        self.refresh_table()

    def refresh_table(self):
        self.table.delete(*self.table.get_children())
        for index, row in self.df.iterrows():
            self.table.insert("", "end", text=index, values=(row["col1"], row["col2"], row["col3"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelApp(root)
    root.mainloop()
