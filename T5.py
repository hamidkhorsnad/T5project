import sqlite3

conn = sqlite3.connect('expenses.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Expenses (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 date TEXT NOT NULL,
                 category TEXT NOT NULL,
                 amount REAL NOT NULL,
                 description TEXT
             )''')


conn.commit()
conn.close()

# //////////////////////////////////////////////////
    
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("INSERT INTO Expenses (date, category, amount, description) VALUES (?, ?, ?, ?)", 
              (date, category, amount, description))
    conn.commit()
    conn.close()
    print("Expense added successfully!")

def view_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Expenses")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

def update_expense():
    expense_id = int(input("Enter the ID of the expense to update: "))
    date = input("Enter new date (YYYY-MM-DD): ")
    category = input("Enter new category: ")
    amount = float(input("Enter new amount: "))
    description = input("Enter new description: ")

    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("UPDATE Expenses SET date = ?, category = ?, amount = ?, description = ? WHERE id = ?", 
              (date, category, amount, description, expense_id))
    conn.commit()
    conn.close()
    print("Expense updated successfully!")

def delete_expense():
    expense_id = int(input("Enter the ID of the expense to delete: "))

    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("DELETE FROM Expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    print("Expense deleted successfully!")

def main():
    while True:
        print("Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            update_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


