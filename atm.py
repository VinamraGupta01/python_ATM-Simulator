import sqlite3
import tkinter as tk
from tkinter import messagebox

# CONNECT TO DATABASE
conn = sqlite3.connect('atm.db')
cur = conn.cursor()

# CREATE ACCOUNTS TABLE IF NOT EXISTS
cur.execute('''
CREATE TABLE IF NOT EXISTS ACCOUNTS (
    ACC_NO INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    PIN TEXT NOT NULL,
    BALANCE REAL DEFAULT 0
)
''')
conn.commit()

# FUNCTION TO CREATE A NEW ACCOUNT
def create_account(name, pin, balance):
    cur.execute("INSERT INTO ACCOUNTS (NAME, PIN, BALANCE) VALUES (?, ?, ?)", (name, pin, balance))
    conn.commit()

# FUNCTION TO LOGIN
def login(acc_no, pin):
    cur.execute("SELECT * FROM ACCOUNTS WHERE ACC_NO = ? AND PIN = ?", (acc_no, pin))
    return cur.fetchone()

# FUNCTION TO GET BALANCE
def get_balance(acc_no):
    cur.execute("SELECT BALANCE FROM ACCOUNTS WHERE ACC_NO = ?", (acc_no,))
    return cur.fetchone()[0]

# FUNCTION TO DEPOSIT
def deposit(acc_no, amount):
    cur.execute("UPDATE ACCOUNTS SET BALANCE = BALANCE + ? WHERE ACC_NO = ?", (amount, acc_no))
    conn.commit()

# FUNCTION TO WITHDRAW
def withdraw(acc_no, amount):
    current_balance = get_balance(acc_no)
    if amount > current_balance:
        return False
    cur.execute("UPDATE ACCOUNTS SET BALANCE = BALANCE - ? WHERE ACC_NO = ?", (amount, acc_no))
    conn.commit()
    return True

# === GUI START ===

class ATMApp:
    def __init__(self, master):
        self.master = master
        master.title("ATM Simulator")
        master.geometry("400x400")
        master.configure(bg="#f2f2f2")
        self.acc_no = None
        self.login_screen()

    def login_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="ATM LOGIN", font=("Arial", 20), bg="#f2f2f2").pack(pady=20)

        tk.Label(self.master, text="Account No:", bg="#f2f2f2").pack()
        self.acc_entry = tk.Entry(self.master)
        self.acc_entry.pack()

        tk.Label(self.master, text="PIN:", bg="#f2f2f2").pack()
        self.pin_entry = tk.Entry(self.master, show="*")
        self.pin_entry.pack()

        tk.Button(self.master, text="Login", command=self.handle_login, bg="#4CAF50", fg="white").pack(pady=10)

    def handle_login(self):
        acc_no = self.acc_entry.get()
        pin = self.pin_entry.get()
        if acc_no.isdigit():
            user = login(int(acc_no), pin)
            if user:
                self.acc_no = int(acc_no)
                self.main_menu(user[1])
            else:
                messagebox.showerror("Login Failed", "Invalid Account No or PIN")
        else:
            messagebox.showerror("Error", "Invalid input")

    def main_menu(self, name):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text=f"Welcome, {name}", font=("Arial", 16), bg="#f2f2f2").pack(pady=20)

        tk.Button(self.master, text="Check Balance", command=self.show_balance, width=20).pack(pady=5)
        tk.Button(self.master, text="Deposit", command=self.deposit_money, width=20).pack(pady=5)
        tk.Button(self.master, text="Withdraw", command=self.withdraw_money, width=20).pack(pady=5)
        tk.Button(self.master, text="Logout", command=self.login_screen, width=20).pack(pady=20)

    def show_balance(self):
        balance = get_balance(self.acc_no)
        messagebox.showinfo("Balance", f"Your current balance is: ₹{balance}")

    def deposit_money(self):
        def process_deposit():
            try:
                amt = float(entry.get())
                if amt > 0:
                    deposit(self.acc_no, amt)
                    messagebox.showinfo("Success", f"₹{amt} deposited successfully!")
                    top.destroy()
                else:
                    messagebox.showerror("Error", "Amount must be greater than 0")
            except:
                messagebox.showerror("Error", "Invalid amount")

        top = tk.Toplevel(self.master)
        top.title("Deposit")
        tk.Label(top, text="Enter amount to deposit:").pack(pady=10)
        entry = tk.Entry(top)
        entry.pack()
        tk.Button(top, text="Deposit", command=process_deposit).pack(pady=10)

    def withdraw_money(self):
        def process_withdraw():
            try:
                amt = float(entry.get())
                if amt > 0:
                    success = withdraw(self.acc_no, amt)
                    if success:
                        messagebox.showinfo("Success", f"₹{amt} withdrawn successfully!")
                        top.destroy()
                    else:
                        messagebox.showerror("Error", "Insufficient balance")
                else:
                    messagebox.showerror("Error", "Amount must be greater than 0")
            except:
                messagebox.showerror("Error", "Invalid amount")

        top = tk.Toplevel(self.master)
        top.title("Withdraw")
        tk.Label(top, text="Enter amount to withdraw:").pack(pady=10)
        entry = tk.Entry(top)
        entry.pack()
        tk.Button(top, text="Withdraw", command=process_withdraw).pack(pady=10)


# CREATE TEST ACCOUNT IF NOT EXISTS
cur.execute("SELECT * FROM ACCOUNTS WHERE NAME = 'VINAMRA GUPTA'")
if not cur.fetchone():
    create_account("VINAMRA GUPTA", "999070", 10000)

# RUN APP
root = tk.Tk()
app = ATMApp(root)
root.mainloop()

# CLOSE DATABASE
conn.close()
