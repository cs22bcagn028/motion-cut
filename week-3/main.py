import tkinter as tk
from tkinter import messagebox
from collections import defaultdict
from tkcalendar import DateEntry
from datetime import datetime

class ExpenseTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        self.expenses = defaultdict(list)

        self.expense_name_label = tk.Label(master, text="Expense Name:")
        self.expense_name_label.grid(row=0, column=0, sticky="e")
        self.expense_name_entry = tk.Entry(master)
        self.expense_name_entry.grid(row=0, column=1)

        self.date_label = tk.Label(master, text="Date:")
        self.date_label.grid(row=1, column=0, sticky="e")
        self.date_entry = DateEntry(master, date_pattern="YYYY-MM-DD")
        self.date_entry.grid(row=1, column=1)

        self.category_label = tk.Label(master, text="Expense Category:")
        self.category_label.grid(row=2, column=0, sticky="e")
        self.category_var = tk.StringVar(master)
        self.category_var.set("Select Category")
        self.category_menu = tk.OptionMenu(master, self.category_var, "Food", "Transport", "Entertainment")
        self.category_menu.grid(row=2, column=1)

        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.grid(row=3, column=0, sticky="e")
        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=3, column=1)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_expense)
        self.submit_button.grid(row=4, columnspan=2)

        self.summary_button = tk.Button(master, text="Summarize", command=self.summarize_expenses)
        self.summary_button.grid(row=5, columnspan=2)

        self.category_button = tk.Button(master, text="Category wise", command=self.category_wise_expenses)
        self.category_button.grid(row=6, columnspan=2)

    def submit_expense(self):
        name = self.expense_name_entry.get()
        date = self.date_entry.get()
        category = self.category_var.get()
        amount = self.amount_entry.get()

        if not name or not date or not category or not amount:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return

        self.expenses[date].append((name, category, amount))
        messagebox.showinfo("Success", "Expense added successfully.")

        self.expense_name_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def summarize_expenses(self):
        monthly_expenses = defaultdict(float)
        for date, expenses in self.expenses.items():
            month = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m")
            total_expense = sum(expense[2] for expense in expenses)
            monthly_expenses[month] += total_expense

        message = "Total expenses for different months:\n"
        for month, total_expense in monthly_expenses.items():
            message += f"{month}: ${total_expense:.2f}\n"

        messagebox.showinfo("Monthly Expenses Summary", message)

    def category_wise_expenses(self):
        category_expenses = defaultdict(float)
        for expenses in self.expenses.values():
            for expense in expenses:
                category_expenses[expense[1]] += expense[2]

        message = "Category wise total expenses:\n"
        for category, total in category_expenses.items():
            message += f"{category}: ${total:.2f}\n"

        messagebox.showinfo("Category Wise Expenses", message)


def main():
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()


if __name__ == "__main__":
    main()
