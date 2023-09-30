import math
import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.entry = None
        self.root = root
        self.root.title("Calculator")

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, width=30, font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('**', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('trig', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('C', 4, 4),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=('Arial', 16), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        # Configure row and column weights for button resizing
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = self.evaluate_expression(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif value == 'sqrt':
            try:
                result = self.calculate_square_root(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif value == '**':
            self.entry.insert(tk.END, '**')
        elif value == 'trig':
            try:
                result = self.calculate_trig(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif value == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, value)

    def evaluate_expression(self, expression):
        try:
            return eval(expression)
        except Exception:
            raise ValueError("Invalid expression")

    def calculate_square_root(self, value):
        if value >= 0:
            return math.sqrt(value)
        else:
            raise ValueError("Cannot calculate square root of a negative number.")

    def calculate_trig(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        sine = math.sin(angle_radians)
        cosine = math.cos(angle_radians)
        tangent = math.tan(angle_radians)
        return f"Sine: {sine:.4f}, Cosine: {cosine:.4f}, Tangent: {tangent:.4f}"


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
