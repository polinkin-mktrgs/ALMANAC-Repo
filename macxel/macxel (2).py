import tkinter as tk

class SumTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Macxel")

        self.entries = []

        # Создаем таблицу с 20 строками и 10 столбцами
        for i in range(20):
            row_entries = []
            for j in range(10):
                entry = tk.Entry(root, width=15)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

        # Кнопка для вычисления суммы
        self.calculate_sum_button = tk.Button(root, text="Вычислить сумму", command=self.calculate_sum)
        self.calculate_sum_button.grid(row=20, column=0, pady=10)

        # Кнопка для умножения
        self.multiply_button = tk.Button(root, text="Умножить", command=self.multiply_entries)
        self.multiply_button.grid(row=20, column=1, pady=10)

        # Кнопка для вычитания
        self.subtract_button = tk.Button(root, text="Вычесть", command=self.subtract_entries)
        self.subtract_button.grid(row=20, column=2, pady=10)

        # Кнопка для очистки данных
        self.clear_button = tk.Button(root, text="Очистить данные", command=self.clear_entries)
        self.clear_button.grid(row=20, column=3, pady=10)

        # Текстовое поле для отображения суммы
        self.sum_label = tk.Label(root, text="Сумма: 0")
        self.sum_label.grid(row=20, column=4, pady=10)

    def calculate_sum(self):
        total_sum = 0
        for row_entries in self.entries:
            for entry in row_entries:
                try:
                    value = float(entry.get())  # Пробуем преобразовать значение в число
                    total_sum += value
                except ValueError:
                    continue  # Игнорируем ячейки с недопустимыми значениями

        self.sum_label.config(text=f"Сумма: {total_sum}")

    def multiply_entries(self):
        product = 1
        for row_entries in self.entries:
            for entry in row_entries:
                try:
                    value = float(entry.get())  # Пробуем преобразовать значение в число
                    product *= value
                except ValueError:
                    continue  # Игнорируем ячейки с недопустимыми значениями

        self.sum_label.config(text=f"Произведение: {product}")

    def subtract_entries(self):
        difference = 0
        for row_entries in self.entries:
            for entry in row_entries:
                try:
                    value = float(entry.get())  # Пробуем преобразовать значение в число
                    difference -= value
                except ValueError:
                    continue  # Игнорируем ячейки с недопустимыми значениями

        self.sum_label.config(text=f"Разность: {difference}")

    def clear_entries(self):
        for row_entries in self.entries:
            for entry in row_entries:
                entry.delete(0, tk.END)  # Очищаем текстовое поле

        self.sum_label.config(text="Сумма: 0")  # Сбрасываем сумму

if __name__ == "__main__":
    root = tk.Tk()
    app = SumTableApp(root)
    root.mainloop()
