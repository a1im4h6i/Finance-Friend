import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
from datetime import date, datetime

class FinanceFriendApp:
    # The main application class groups together all GUI logic, data access, and application state
    # Keeping this as a class supports modularity and allows a different programmer to reuse
    # the business logic separately from the Tkinter root window
    def __init__(self, root):
        self.root = root
        self.root.title("FinanceFriend - Student Budgeting")
        self.root.geometry("400x400")
        self.root.configure(bg="#baeeb7")
        
        # Application state variables are stored here so methods can share user-specific data
        self.current_user_id = None
        self.budget_limit = 0.0

        # ttk styling is configured once to make all buttons consistent and accessible
        self.style = ttk.Style(self.root)
        try:
            self.style.theme_use('clam')
        except tk.TclError:
            pass
        self.style.configure('Primary.TButton', foreground='white', background='#2563eb', font=("Arial", 10, "bold"), borderwidth=0, padding=8)
        self.style.map('Primary.TButton', background=[('active', '#1d4ed8'), ('pressed', '#1e40af')], foreground=[('active', 'white')])
        self.style.configure('Secondary.TButton', foreground='white', background='#059669', font=("Arial", 10, "bold"), borderwidth=0, padding=8)
        self.style.map('Secondary.TButton', background=[('active', '#047857'), ('pressed', '#065f46')], foreground=[('active', 'white')])
        self.style.configure('Warning.TButton', foreground='black', background='#f97316', font=("Arial", 10, "bold"), borderwidth=0, padding=8)
        self.style.map('Warning.TButton', background=[('active', '#ea580c'), ('pressed', '#c2410c')], foreground=[('active', 'black')])
        self.style.configure('Danger.TButton', foreground='white', background='#ef4444', font=("Arial", 10, "bold"), borderwidth=0, padding=8)
        self.style.map('Danger.TButton', background=[('active', '#b91c1c'), ('pressed', '#991b1b')], foreground=[('active', 'white')])

        # Database initialization is separated from the UI setup to enforce the separation of concerns.
        # This makes maintenance easier and means the app can build its data model before showing the login screen.
        self.init_db()
        self.create_login_window()

    def init_db(self):
        # Establish the database if it doesn't exist yet. This method is responsible for the data model.
        conn = sqlite3.connect('financefriend.db')
        cursor = conn.cursor()
        # The users table stores account credentials and budget metadata.
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            points INTEGER DEFAULT 0,
                            budget_limit REAL DEFAULT 0)''')
        # The transactions table uses a FOREIGN KEY to connect each expense back to the correct user.
        # This relational structure is important so the app can query spending per user and maintain data integrity.
        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            amount REAL NOT NULL,
                            category TEXT NOT NULL,
                            date TEXT NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES users(user_id))''')
        conn.commit()
        conn.close()

    def create_login_window(self):
        # Build a simple login screen first so users must authenticate before accessing the app.
        self.root.configure(bg='#eef2ff')
        self.main_frame = tk.Frame(self.root, bg='#eef2ff', padx=25, pady=25)
        self.main_frame.pack(expand=True)

        self.username_entry = tk.Entry(self.main_frame, bg='white', fg='black', insertbackground='black', width=30, font=("Arial", 10))
        self.password_entry = tk.Entry(self.main_frame, show="*", bg='white', fg='black', insertbackground='black', width=30, font=("Arial", 10))

        tk.Label(self.main_frame, text="FinanceFriend Login", fg='#0f172a', bg='#eef2ff', font=("Arial", 16, "bold")).pack(pady=(0, 15))
        tk.Label(self.main_frame, text="Username:", fg='#0f172a', bg='#eef2ff', font=("Arial", 10, "bold")).pack(pady=5)
        self.username_entry.pack(pady=2)

        tk.Label(self.main_frame, text="Password:", fg='#0f172a', bg='#eef2ff', font=("Arial", 10, "bold")).pack(pady=5)
        self.password_entry.pack(pady=2)

        ttk.Button(self.main_frame, text="Login", command=self.validate_login, style='Primary.TButton').pack(pady=15)
        ttk.Button(self.main_frame, text="New User? Sign Up", command=self.open_signup, style='Secondary.TButton').pack()

        # Allow pressing Enter to submit the form, which improves usability.
        self.username_entry.bind("<Return>", lambda event: self.validate_login())
        self.password_entry.bind("<Return>", lambda event: self.validate_login())

    def validate_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        conn = sqlite3.connect('financefriend.db')
        cursor = conn.cursor()
        # Case-insensitive check makes the app easier to use: 'Alice' and 'alice' log in to the same account.
        # This is a usability decision that avoids accidental login failures due to capitalization.
        cursor.execute("SELECT user_id, budget_limit FROM users WHERE LOWER(username)=LOWER(?) AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        # Selection is used here to choose the next action depending on whether the credentials are valid.
        if user:
            self.current_user_id = user[0]
            self.budget_limit = user[1]
            self.main_frame.destroy()
            self.open_main_app()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def open_signup(self):
        signup_win = tk.Toplevel(self.root)
        signup_win.geometry("340x300")
        signup_win.configure(bg='#eef2ff')

        frame = tk.Frame(signup_win, bg='#eef2ff', padx=20, pady=20)
        frame.pack(expand=True, fill='both')

        tk.Label(frame, text="Create a New Account", fg='#0f172a', bg='#eef2ff', font=("Arial", 14, "bold")).pack(pady=(0, 12))
        tk.Label(frame, text="New Username:", fg='#0f172a', bg='#eef2ff', font=("Arial", 10, "bold")).pack(anchor='w')
        u_ent = tk.Entry(frame, bg='white', fg='black', insertbackground='black', width=32, font=("Arial", 10)); u_ent.pack(pady=4)
        tk.Label(frame, text="New Password:", fg='#0f172a', bg='#eef2ff', font=("Arial", 10, "bold")).pack(anchor='w', pady=(10, 0))
        p_ent = tk.Entry(frame, show="*", bg='white', fg='black', insertbackground='black', width=32, font=("Arial", 10)); p_ent.pack(pady=4)

        def reg():
            u, p = u_ent.get().strip(), p_ent.get().strip()
            if u and p:
                conn = sqlite3.connect('financefriend.db')
                try:
                    conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (u, p))
                    conn.commit()
                    messagebox.showinfo("Success", "Account Created! Please Login.")
                    signup_win.destroy()
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error", "Username exists!")
                conn.close()
            else:
                messagebox.showerror("Error", "Please fill all fields")

        ttk.Button(frame, text="Register", command=reg, style='Primary.TButton').pack(pady=18)
        signup_win.bind("<Return>", lambda event: reg())

    def open_main_app(self):
        self.root.geometry("1100x850")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        self.tab_dashboard = tk.Frame(self.notebook, bg='lightblue')
        self.tab_expenses = tk.Frame(self.notebook, bg='lightgreen')
        self.tab_budget = tk.Frame(self.notebook, bg='lightyellow')
        self.tab_settings = tk.Frame(self.notebook, bg='lightgray')

        self.notebook.add(self.tab_dashboard, text=' Dashboard ')
        self.notebook.add(self.tab_expenses, text=' Expenses ')
        self.notebook.add(self.tab_budget, text=' Budget ')
        self.notebook.add(self.tab_settings, text=' Settings ')

        # All labels set to fg='black'
        self.points_label = tk.Label(self.tab_dashboard, text="Points: 0 🏆", font=("Arial", 16, "bold"), bg='lightblue', fg='black')
        self.points_label.pack(pady=10)
        self.graph_frame = tk.Frame(self.tab_dashboard, bg='lightblue')
        self.graph_frame.pack(expand=True, fill='both')
        
        self.update_points_display()
        self.setup_expenses_tab()
        self.setup_budget_tab()
        self.setup_settings_tab()
        self.update_budget_summary()

    def setup_budget_tab(self):
        tk.Label(self.tab_budget, text="Monthly Budget", font=("Arial", 14, "bold"), bg='lightyellow', fg='black').pack(pady=20)
        tk.Label(self.tab_budget, text="Set a spending limit for the current month and track your progress below.", font=("Arial", 10), bg='lightyellow', fg='black').pack(pady=(0, 15))

        # The budget tab displays both the stored limit and the calculated spending for the month.
        self.limit_display = tk.Label(self.tab_budget, text=f"Current Limit: £{self.budget_limit}", font=("Arial", 12, "bold"), bg='lightyellow', fg='black')
        self.limit_display.pack(pady=(0, 5))
        self.month_spent_label = tk.Label(self.tab_budget, text="This month spent: £0.00", font=("Arial", 12), bg='lightyellow', fg='black')
        self.month_spent_label.pack(pady=2)
        self.remaining_label = tk.Label(self.tab_budget, text="Remaining: £0.00", font=("Arial", 12), bg='lightyellow', fg='black')
        self.remaining_label.pack(pady=2)
        self.budget_status_label = tk.Label(self.tab_budget, text="", font=("Arial", 12, "bold"), bg='lightyellow', fg='black')
        self.budget_status_label.pack(pady=(0, 15))

        self.limit_ent = tk.Entry(self.tab_budget, bg='white', fg='black', insertbackground='black', width=25, font=("Arial", 10)); self.limit_ent.pack(pady=10)
        self.limit_ent.insert(0, str(self.budget_limit if self.budget_limit != 0 else ""))
        
        def save_limit():
            try:
                new_limit = float(self.limit_ent.get())
                conn = sqlite3.connect('financefriend.db')
                conn.execute("UPDATE users SET budget_limit = ? WHERE user_id = ?", (new_limit, self.current_user_id))
                conn.commit(); conn.close()
                self.budget_limit = new_limit
                self.limit_display.config(text=f"Current Limit: £{self.budget_limit}")
                self.update_budget_summary()
                messagebox.showinfo("Success", "Budget Updated!")
            except ValueError:
                # Selection handles the case where the user input is invalid, improving robustness.
                messagebox.showerror("Error", "Enter a valid number")

        ttk.Button(self.tab_budget, text="Save Limit", command=save_limit, style='Warning.TButton').pack(pady=(0, 10))
        ttk.Button(self.tab_budget, text="Refresh Budget", command=self.refresh_budget_tab, style='Secondary.TButton').pack()
        self.limit_ent.bind("<Return>", lambda event: save_limit())

    def setup_expenses_tab(self):
        tk.Label(self.tab_expenses, text="Input Monthly Data", font=("Arial", 14, "bold"), bg='lightgreen', fg='black').pack(pady=10)
        tk.Label(self.tab_expenses, text="Salary (£):", bg='lightgreen', fg='black').pack()
        self.sal_ent = tk.Entry(self.tab_expenses, bg='white', fg='black', insertbackground='black', width=30); self.sal_ent.pack()
        tk.Label(self.tab_expenses, text="Categories (e.g. Food, Rent):", bg='lightgreen', fg='black').pack(pady=(10,0))
        self.cat_ent = tk.Entry(self.tab_expenses, bg='white', fg='black', insertbackground='black', width=30); self.cat_ent.pack()
        tk.Label(self.tab_expenses, text="Costs (£):", bg='lightgreen', fg='black').pack(pady=(10,0))
        self.val_ent = tk.Entry(self.tab_expenses, bg='white', fg='black', insertbackground='black', width=30); self.val_ent.pack()
        ttk.Button(self.tab_expenses, text="Update Dashboard", command=self.process_data, style='Warning.TButton').pack(pady=20)

        self.sal_ent.bind("<Return>", lambda event: self.process_data())
        self.cat_ent.bind("<Return>", lambda event: self.process_data())
        self.val_ent.bind("<Return>", lambda event: self.process_data())

    def setup_settings_tab(self):
        tk.Label(self.tab_settings, text="Settings", font=("Arial", 16), bg='lightgray', fg='black').pack(pady=20)
        ttk.Button(self.tab_settings, text="Logout", command=self.root.destroy, style='Danger.TButton').pack(pady=10)

    def update_points_display(self):
        conn = sqlite3.connect('financefriend.db')
        cursor = conn.cursor()
        cursor.execute("SELECT points FROM users WHERE user_id = ?", (self.current_user_id,))
        p = cursor.fetchone()[0]
        conn.close()
        self.points_label.config(text=f"Score: {p} Points 🏆")

    def load_budget_limit(self):
        conn = sqlite3.connect('financefriend.db')
        cursor = conn.cursor()
        cursor.execute("SELECT budget_limit FROM users WHERE user_id = ?", (self.current_user_id,))
        row = cursor.fetchone()
        conn.close()
        if row is not None:
            self.budget_limit = row[0] or 0.0
        else:
            self.budget_limit = 0.0

    def refresh_budget_tab(self):
        self.load_budget_limit()
        self.limit_ent.delete(0, tk.END)
        if self.budget_limit != 0:
            self.limit_ent.insert(0, f"{self.budget_limit:.2f}")
        self.update_budget_summary()

    def get_monthly_spending(self):
        # Retrieve all transactions for the current user, then calculate monthly spending.
        # This uses iteration to filter by the current month and year, which is an important
        # example of computational thinking in the form of a loop over stored records.
        conn = sqlite3.connect('financefriend.db')
        cursor = conn.cursor()
        cursor.execute("SELECT amount, date FROM transactions WHERE user_id = ?", (self.current_user_id,))
        rows = cursor.fetchall()
        conn.close()
        current_year = date.today().year
        current_month = date.today().month
        total = 0.0
        for amount, date_str in rows:
            try:
                txn_date = datetime.fromisoformat(date_str).date()
                if txn_date.year == current_year and txn_date.month == current_month:
                    total += amount
            except Exception:
                # If the stored date is malformed, fall back to including the amount
                # rather than crashing, which helps maintain application stability.
                total += amount
        return total

    def update_budget_summary(self):
        spent = self.get_monthly_spending()
        remaining = self.budget_limit - spent
        self.limit_display.config(text=f"Current Limit: £{self.budget_limit}")
        self.month_spent_label.config(text=f"This month spent: £{spent:.2f}")
        self.remaining_label.config(text=f"Remaining: £{remaining:.2f}")
        if self.budget_limit == 0:
            self.budget_status_label.config(text="No budget limit set yet.", fg='black')
        elif remaining >= 0:
            self.budget_status_label.config(text="You are on track!", fg='green')
        else:
            self.budget_status_label.config(text="Over budget! Review your spending.", fg='red')

    def process_data(self):
        try:
            salary = float(self.sal_ent.get())
            labels = [l.strip() for l in self.cat_ent.get().split(',')]
            costs = [float(x) for x in self.val_ent.get().split(',')]
            
            conn = sqlite3.connect('financefriend.db')
            cursor = conn.cursor()
            today = date.today().isoformat()
            for c, v in zip(labels, costs):
                cursor.execute("INSERT INTO transactions (user_id, amount, category, date) VALUES (?, ?, ?, ?)", (self.current_user_id, v, c, today))
            cursor.execute("UPDATE users SET points = points + 10 WHERE user_id = ?", (self.current_user_id,))
            conn.commit(); conn.close()

            self.update_points_display()
            self.update_budget_summary()
            self.draw_graphs(salary, labels, costs)
            self.notebook.select(self.tab_dashboard)
        except:
            messagebox.showerror("Error", "Invalid Data")

    def draw_graphs(self, salary, labels, costs):
        #clear previous graphs to prevent memory overlap and UI clutter
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        total_spent = sum(costs)
        fig, axs = plt.subplots(1, 3, figsize=(14, 5))
        fig.patch.set_facecolor('lightblue')

        #bar chart: comparing fixed salary to total costs
        axs[0].bar(['Salary', 'Spent', 'Limit'], [salary, total_spent, self.budget_limit], color=['blue', 'red', 'orange'])
        axs[0].set_title("Budget Overview", color='black')

        #pie chart: breakdown of expenses by category
        axs[1].pie(costs, labels=labels, autopct='%1.1f%%', textprops={'color':"black"})
        axs[1].set_title("Spending %", color='black')

        #line plot: tracking spending against budget limit and actual spending
        axs[2].plot(['Limit', 'Actual'], [self.budget_limit, total_spent], marker='o', color='green' if total_spent <= self.budget_limit else 'red')
        axs[2].set_title("Goal Tracking", color='black')

        #embed the plot into the Tkinter dashboard
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceFriendApp(root)
    root.mainloop()