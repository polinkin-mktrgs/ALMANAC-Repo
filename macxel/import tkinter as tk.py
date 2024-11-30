import tkinter as tk
from tkinter import messagebox
from math import*

class LargeTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("macxel")

        self.entries = []

        # Создаем таблицу с 20 строками и 10 столбцами
        for i in range(20):
            row_entries = []
            for j in range(10):
                entry = tk.Entry(root, width=15)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

        # Кнопка для получения данных из таблицы
        self.get_data_button = tk.Button(root, text="Получить данные", command=self.get_data)
        self.get_data_button.grid(row=20, column=0, pady=10)

        # Кнопка для очистки таблицы
        self.clear_button = tk.Button(root, text="Очистить таблицу", command=self.clear_table)
        self.clear_button.grid(row=20, column=1, pady=10)
        # Кнопка сумма
        self.calculate_sum_button = tk.Button(root, text="Вычислить сумму", command=self.calculate_sum)
        self.calculate_sum_button.grid(row=20, column=2, pady=10)

        # Текстовое поле для отображения данных
        self.text_output = tk.Text(root, height=10, width=80)
        self.text_output.grid(row=21, columnspan=10, padx=5, pady=5)

    def get_data(self):
        data = []
        for row_entries in self.entries:
            row_data = [entry.get() for entry in row_entries]
            data.append(row_data)

        self.text_output.delete(1.0, tk.END)  # Очистить текстовое поле
        for row in data:
            self.text_output.insert(tk.END, ', '.join(row) + '\n')

    def clear_table(self):
        for row_entries in self.entries:
            for entry in row_entries:
                entry.delete(0, tk.END)  # Очистить каждую ячейку

        self.text_output.delete(1.0, tk.END)  # Очистить текстовое поле

        self.sum_label = tk.Label(root, text="Сумма: 0")
        self.sum_label.grid(row=20, column=3, pady=10)

    def calculate_sum(self):
        total_sum = 0
        for row_entries in self.entries:
            for entry in row_entries:
                try:
                    value = float(entry.get())  # Пробуем преобразовать значение в число
                    total_sum += value
                except ValueError:
                    continue  # Игнорируем ячейки с недопустимыми значениями

if __name__ == "__main__":
    root = tk.Tk()
    app = LargeTableApp(root)
    root.mainloop()