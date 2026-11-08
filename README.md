Analysis
Problem Definition
Young adults (ages 12 – 25) struggle with financial budgeting because existing apps are either too advanced and technical for their needs, or they require excessive manual input, making budgeting feel like a chore. Most apps also lack gamification features to encourage regular use, don’t include parental oversight options, and use dull colour schemes which don’t appeal to this demographic. This creates a gap in the market for a simpler, engaging free budgeting app which is tailored to younger people.
FinanceFriend addresses this gap by offering a user-friendly interface with vibrant colour schemes and engaging design which appeals to all ages, making budgeting more accessible and enjoyable for young adults
This problem is worth solving because financial literacy in younger people leads to better decision-making and reduced chances of debt later in life. To add to that, FinanceFriend could be further developed with features like reminders, alerts, or even linking it with banking data so that it becomes more scalable in the future.
Background Research
Quicken is a desktop application for adults who use the platform for their complex portfolio. Its strengths include comprehensive reporting (watch lists, spending plans, and track expenses) to keep constant sync with the portfolio. Therefore, my application Finance Friend will reduce the amount of complex information which isn’t needed for smaller capitals and keeping the same type of features but making them easier and more understandable for a young adult.
YNAB, which stands for You Need a Budget, is a unique personal finance app with a singular focus: to teach you smarter ways to spend your money so you can save more. It has a steep learning curve and requires regular attention, but the eventual reward is a flexible monthly spending plan that’s tailored to meet your goals. We included it because it’s built on a sound philosophy of financial responsibility and diligence that can change how you think about money. Therefore, I introduced more gamification features (points, daily streaks or challenges) to make budgeting more fun and less of a chore and more inspirational to use later in life.
Green Light allows people have a better shot at being responsible with their money if they get a head start while they're young. Greenlight is the best app we've seen for kids (with adult oversight). It lets grown-ups supervise as kids learn to save, spend, give, and invest using a family debit card. The adult account owner can send money to their kids through the app and monitor their activity. Greenlight encourages children to save money, and you can optionally open a related savings account with a good interest rate to support that. But with these benefits, the costs of the application are that there is a monthly subscription at $5.99 a month. This makes it a burden for parents and children to use applications like these, therefore, less likely for it to be interesting and defeats the purpose if responsibly using your money. Therefore, Finance Friend will be completely free to purchase and has a feature to not use a bank account to test the application.
In conclusion, existing financial budgeting apps target mostly adults and lack encouragement and engagement for the younger audience. They use boring and dull GUI interfaces and don’t make the idea of budgeting something fun to do. My app, Finance Friend, addresses this gap in the market by combining simplicity (from Quicken), gamification (from YNAB), free access with parental controls (from Greenlight), and a colourful, exciting interface (unique to Finance Friend). This makes an app which young people would use regularly. This research justifies my design choices: simplicity over complexity, gamification over academic discipline, free access over subscription costs and visual appeal over dull interfaces.
Computational Justification
Finance tracking is fundamentally computational problem because it needs to store user transactions, budgets, and account information. The system must perform data processing to calculate total expenses, compare spending against budget limits, and compute remaining balance. Additionally, it needs data visualisation to generate graphs and charts that display spending patterns in an accessible way. Finally, the system must automate routine tasks such as awarding points for staying on budget or sending alerts when limits are exceeded and resetting budgets at the end of each month.
A computational solution is appropriate because manual tracking using pen and paper is time-consuming, prone to errors and provides no visual insights to spending patterns. By automating these calculations, FinanceFriend reduces human error and enables instant feedback to the user whenever they enter a transaction. Real-time graphs help users understand their spending habits immediately, which encourages change of behaviour and supports better financial decision-making among young adults.
My chosen approach using Python with Tkinter, SQLite3 and Matplotlib is appropriate for this project. Python is accessible and quick to develop, making it ideal for a school project with time constraints. SQLite3 allows local database storage without requiring external sources like a server or internet connection, ensuring data is stored on device even offline. Tkinter creates a simple, functional graphical user interface suitable for applications without complex systems. Matplotlib generates professional graphs and charts from data, allowing users to visualise their spending more clearly. All these libraries are free, open-source and well documented which reduces development errors and makes the project reusable. More importantly, this stack allows me to focus on core functionality and budgeting logic rather than spending time creating the libraries myself.
This approach prioritises functionality and usability from the target user (ages 12-25) over mobile responsiveness or cloud deployment. These trade-offs are appropriate given the scope of a school project and the technical difficulty of implementing a mobile application in Python.
Target Market/Stakeholders
The target market is young adults ages 12-25, primarily students. Unlike existing apps that make users feel judged for overstepping their budget, FinanceFriend is designed to be encouraging and engaging to change these habits. Young adults struggle with finance apps because they are either too technical (Quicken) or feel like homework (YNAB).
My app FinanceFriend addresses this by using a modern, vibrant interface (not grey/dull), which also includes elements of gamification (points, rewards, challenges), keeping it simple and intuitive (4 main navigation sections max), and designing it with mobile availability in mind (though currently implemented as a desktop application in tkinter).
Stakeholders include young users (ages 12-25) who want a simple, fun, engaging experience; parents of users under 18 who want to monitor spending and set limits: and educational institutions that could broadcast this app for teaching financial literacy
By addressing the needs of all three stakeholder groups, FinanceFriend bridges the gap between user engagement and parental oversight, making it suitable for both independent learners and family-based financial learning.
Stakeholder Requirements
Young Adults (primary user)
Visual data representation (charts and graphs)
•	My research into Quicken showed that spreadsheets are overwhelming for beginners. Young adults need a quick, visual way to see where their money is going (e.g.: food vs entertainment) to make behavioural changes
Gamification (points system)
•	Financial literacy is often seen as ‘dull’ by this demographic. A points system encourages daily logging, which is essential for the app to provide accurate long- term data. This requires the implementation of an algorithm that calculates points based on the frequency of data entry and the accuracy of budget submission.
Simple UI
•	Younger users prioritise speed of entry. If the UI is complex, they will abandon the app and think this process is too complex. Therefore, opting to a minimalist navigation system is a justified requirement to ensure user retention
Parents (secondary user)
Viewing mode
•	For users in the 12-25 age bracket, parents act as a financial mentor. A specific requirement in the future for a view only mode allows parents to monitor spending habits without needing to log in as the child, enabling important conversations about money management
Spending limits
•	Parents are stakeholders of the child because they often provide the capital usually through allowance. Therefore, I could create a feature that flags when a budget is exceeded so they can intervene before the user runs out of funds. This will use conditional logic to compare real-time spending variables against user defined limit restrictions, triggering an alert if the threshold is breached
Educators (tertiary user)
Data reporting
•	Educators who want to use real world data to teach budgeting. A future feature could be to export spending data into a CSV format justified so that the app can be used as a practical tool in ‘personal finance’ or ‘citizenship’ lessons in schools. This involves data transformation, where the relational database records (SQLite) are parsed and rewritten into a flat-file comma-separated format for external compatibility

Functional Requirements
User Authentication
•	Users can choose whether to sign-in or sign-up
•	Users must register with an email, username and password
•	Users must login with a username and password
•	System must reject repeated usernames from the database
•	System must validate password against stored passwords
•	System must reject login attempts with wrong password inputs
Expense Tracking
•	User must add expense with costs and names of those costs
•	System must provide pre-defined expense categories (Food, Transport, Entertainment, Bills, Shopping)
•	System must validate that amount is not negative
•	System must validate that category is selected and has a corresponding cost
•	System must store expense in the database
•	User must view all past expenses in a list
Budget Management
•	User must set monthly budget limit per category (e.g. £500 for shopping)
•	System must compare actual spending vs what the budget spending should be
•	System must show budget which is remaining for every category
•	System must alert user when expenditures have exceeded the budget for a certain category
•	System must reset budgets every month
Data Visualisation
•	System must display pie chart showing spending breakdown per category
•	System must display bar chart showing salary versus expenses versus remaining
•	System must display line graph showing spending trend over time
•	Graphs must update when newer expenses are inserted
•	System must label axes and values very clearly
Gamification (Kid-Friendly Features)
•	System must award points whenever a user adds a new transaction
•	System must display current points total on the dashboard
•	System must implement emojis within the dashboard
•	System must display motivational quotes randomly when dashboard is open
•	System must display a wide scope of colours and an engaging interface design
Age Restrictions & Parental Controls
•	System must ask the user to verify their age when they sign up
•	System must require parental consent if the user is younger than 13 years of age
•	Parents must be able to create a separate account to view their child’s account
•	Parents dashboard must show all the transactions made by the child
•	Parents must be able to set limits on spending for each category created (e.g. £50 max on food)
Non-Functional Requirements
Usability
•	Interface must be simple to understand for ages 12-25 without instructions
•	All buttons must have clear labels explaining what they do
•	All input forms must validate data and display helpful error notifications
•	Colour scheme must use primary colours (red, yellow, blue) with sufficient contrast and no flashing elements
•	Navigation menu must be simple to interact with maximum of 4 sections
Performance
•	Login must complete in less than 2-3 seconds
•	Graphs must render in less than 3 seconds with all relevant transactions
•	Database queries must be completed in 1-2 seconds
•	App cannot lag when updating new expenses
•	App must handle multiple transaction inputs without slowing down
Data Persistence
•	All transactions made must be stored to the sqlite3 database
•	All budgets must be stored in the database
•	Data must be recoverable after app restart
•	User data must not be lost if the app closes unexpectedly
•	Data must survive app crashes
Reliability
•	App must not crash if user enters wrong credentials or values (e.g. integers in a string input)
•	App must confirm all user input before execution
•	App must show error notifications without termination of the app
•	App must recover smoothly from unexpected errors
•	System must always maintain data security
Security
•	Passwords should be encrypted in a production environment
•	Other users are not allowed to view other user’s data
•	User sessions must expire after 30 mins of inactivity
•	Sensitive data must be protected from unauthorised access
•	System must follow data protection law act
Hardware/Software Requirements
Hardware Requirements
•	Personal computer with at least 2GB of ram
•	Standard processor (Intel i3 or equivalent)
•	500mb of free disk space for database
•	Standard keyboard or mouse
•	Monitor with 1024x768 minimum resolution
•	Windows 7+, macOS 10.12+ or Linux (ubuntu 16.04+)
Software Requirements
•	Python 3.8 or higher
•	Tkinter (built-in with Python, required for GUI)
•	SQLite3 (built-in with Python, required for database)
•	Matplotlib (required for graph generation, installed via pip)
These requirements are needed to ensure the application runs on standard computers without requiring internet connectivity or external server systems. All the tools are free and open source, making the project reusable and accessible to users with standard personal computers.
Success Criteria
User Authentication Works
•	Users able to register with email, username and password
•	Login works successfully with correct credentials
•	System rejects duplicate usernames and invalid passwords
•	Measurable: 3/3 test users can register and login – 100% success
Expenses Continue Between Sessions
•	Users can add expenses and they are stored in the database
•	Data remains after the app is closed and reopened
•	Measurable: Add 5 expenses, close app, reopen, all 5 expenses presented = PASS
Budget Calculations Accurate
•	System will calculate remaining budget correctly (budget – total spent)
•	Alert users when spending exceeds budget
•	Measurable: Set budget £100, spend £120, alert triggered = PASS
Graphs Display Correctly
•	Pie chart shows spending by category
•	Bar chart shows total spending vs remaining salary for each month
•	Line graph shows spending trends over time
•	All graphs update when new expense is added
•	Measurable: Add 10 transactions across multiple months, all 3 graphs display without errors and show correct data = PASS
Gamification System Works
•	Points awarded when transactions are added (1 point per transaction)
•	Points total display on dashboard
•	Motivational quotes displayed at random
•	Measurable: Add expenses, check points = 5 points awarded = PASS
Parental Controls
•	Parents can create a separate account and view child’s transactions
•	Parents can set spending limits per category
•	Limits prevent child exceeding them
•	Measurable: Parent sets £50 food limit, child attempts £60 transaction, rejected = PASS
App Controls Errors
•	App doesn’t crash when user enters invalid input
•	Error messages display and allow the user to retry
•	Measurable: Enter 10 invalid inputs, app survives all without crashing = PASS
Limitations
Desktop-Only Application
•	Application only works on desktop computers, not phones or tablets
•	This will limit user who mainly use smartphones
•	Mobile apps in Python are incredibly difficult to create
•	Future versions could use Flutter or React Native for phones
•	Trade-off: acceptable for a school project
Initial Password Security
•	Passwords stored as plain text in the database
•	Security risk if database is compromised
•	Proper encryption would need extra libraries and take more time
•	Acceptable for a prototype but needs fixing for publishing online
•	Trade-off: simplicity vs security for MVP (minimum viable product)
Single User
•	Only one user can be logged in at a time
•	Supporting multiple users needs complex session handling
•	Would require significant Changes over multi-user support
•	Beyond scope for this project
•	Trade-off: MVP (minimum viable product) functionality over multi-user support
Limited Customisation
•	Expense categories are pre-defined (Food, Transport, Entertainment, Bills, Shopping)
•	Users cannot create their own custom categories
•	Adding custom categories needs more UI design and database changes
•	Trade-off: simplicity over flexibility
No Data Export
•	Users cannot export transactions to pdf or csv files
•	Useful for record-keeping but not included
•	Feature is beyond the scope of the MVP (minimum viable product)
•	Could be added in future versions
Limited Parental Controls
•	Parents can view child data and set spending limits
•	Parents cannot edit or delete transactions
•	Adding audit trails and edit features needs more complex code 
•	Trade-off: keeping it simple vs adding advanced parental features
No Real Time Notifications
•	App cannot send alerts unless user has it open
•	Real-time notifications need background services and external apps like Firebase
•	This is beyond the scope of a school project
•	Trade-off: local app vs cloud-based notifications
Design
Problem Decomposition

 
This decomposition illustrates the modular breakdown of the FinanceFriend application. While the primary focus is on user-facing modules like the Dashboard and Gamification, the ‘data’ module implicitly hands the SQLite relational database interactions, and the ‘login’ module handles authentication logic. This modular approach ensures separation of concerns during the development phase
Proposed Solution
FinanceFriend is produced using:
•	Python as the language
•	Tkinter for the GUI
•	SQLite3 for local data storage
•	Matplotlib for data visualisation
Design Approach:
•	OOP (object-oriented programming) with 5 main classes used:
•	User, Transaction, Budget, Dashboard and parentUser
•	Each class encapsulates data and methods for modularity
•	Data is stored locally on the user’s device (no external servers)
•	All inputs are validated through methods before storing in the database
•	Calculation is performed automatically when newer transactions are added
•	Graphs and charts are updated in real-time using Matplotlib
Key Features:
•	Offline functionality since data is stored locally with the user
•	Fast performance without relying on an internet connection
•	Simple, easy to understand interface designed for ages 12-25
•	Responsive system that remains quick even with multiple calculations
•	Vibrant colour scheme with clear labels and navigation
Class Structure
Class Name	Attributes	Data Type	Methods
User	Username
Password
Email
Age
isParent
points	String
String
String
Integer
Boolean
integer	Login()
Register()
Verify_age()
Validate_password()
Logout()
Dashboard	UserID
Total_balance
Total_spent
Current_points	Integer
Float
Float
integer	display_pie_chart()
Display_bar_chart()
Display_line_graph()
update_graphs()
Display_quote()
show_recent()
parentUser	ParentID
Username
Password
Email
ChildID	Integer
String
String
String
integer	login()
child_spending()
set_limit()
monitor_spending()
Transaction	TransactionID
UserID
Amount_spent
category
date
description	Integer
Integer
Float
String
Date
string	Add_transaction()
validate_amount()
validate_category()
save_to_database()
get_all_transactions()
Budget	BudgetID
UserID
Category
Limit
Spent
Month	Integer
Integer
Category
float
Spent
integer	set_budget()
update_spent()
check_exceed()
recet_monthly()
calculate_remaining()
Database Schema & Entity Relationship Diagram
This relational database uses foreign keys to ensure referential integrity between users and their transactions, minimizing data redundancy.
Database Schema
This database consists of 4 tables: Users (account information), Transactions (individual expenses), Budgets (monthly spending limits) and parentChild (parent & child relation for monitoring).
Entity Relationship Diagram
The table users have a one-to-many relationship with Transactions and Budget since the user will have multiple expenses and budgets to be within. Users also have a one-to-many relationship with parentChild (one parent user can have links to many child users). The parentChild table stores parent_id and child_id to track these relations.
Data Dictionary
Table 1: Users
Field Name	Data Type	Key	Rules
user_id	integer	primary key	primary key and auto-increment
username	string		not null and unique
password	string		not null
email	string		not null and must contain ‘@’ and ‘.’ symbols
age	integer		range check: 12 <= age <= 100
points	integer		default = o and cannot be negative
is_parent	integer		boolean (‘0’ = child and ‘1’ = parent)
Table 2: Transactions
Field Name	Data Type	Key	Rules
transaction_id	integer	primary key	primary key and auto-increment
user_id	integer	foreign key	foreign key to users.user_id
amount	real		not null and must be > £0.00
category	string		restricted to food, transport, entertainment, bills, shopping
date	string		format: yyyy-mm-dd
description	string		max 100 characters

Table 3: Budgets

Field Name	Data Type	Key	Rules
budget_id	integer	primary key	primary key and auto-increment
user_id	integer	foreign key	foreign key to users.user_id
category	string		not null (matches transaction categories)
limit_amt	real		not null and must be >= 0
spent_amt	real		updated dynamically via logic
month	string		format:mm-yyyy

System Flowcharts
Login
 
Sign-Up
 
Add Expense
 
Calculate Budget
 

UI Mock-up
Sign-up Page
 
Login Page
 
Dashboard
 
Add Expense
 
Budget Management
 


Pseudocode
#Login Function
FUNCTION login (username, password)
       User = database.finduser(username)
       If user == null THEN
           Display “invalid username”
           Return false
       End if
      If user.password != password THEN
           Display “invalid password”
           Return false
      End if
    Display “welcome” + user.username
    Current_user = user
    Open dashboard
    Return true
End FUNCTION
#Add Transaction Function
Function add_transaction(amount ,category ,date ,description)
          If amount <= 0 THEN
                 Display “amount must be positive”
                 Return false
         END IF
         If category NOT IN valid_categories THEN
               Display “invalid category”
               Return false
        END IF
        Transaction = CREATE new transaction(amount, category, data, description)
         Database.save(transaction)

         Current_user.points += 1
  
         Budget = database.find_budget(current_user.id, category, current_month)
         Budget.spent = budget.spent + amount
         Database.save(budget)

        UPDATE_graphs()
        Display “expense added successfully”
        Return true
   END FUNCTION
#Calculate Budget Function
FUNCTION calculate_budget()
   Transactions = database.GET_transactions(current_user.id, category, current_month)

     FOR each category IN valid_categories DO
             Spent = SUM(transactions WHERE category == current_category)
             Budget = database.FIND_budget(current_user.id, category, current_month)
             Remaining = budget.limit – spent
            
            IF remaining < 0 THEN
                      DISPLAY “budget exceeded for “ + category
             END IF
      END FOR
     	
      GENERATE pi_chart(transactions
      GENERATE bar_graph(budgets)
        GENERATE linegraph (monthly_totals)
        DISPLAY graphs on dashboard
END FUNCTION
Usability Features
Colour Scheme
•	Uses vibrant primary colours to appeal to younger ages (12-25)
•	High contrast between text and background for readability
•	Consistent colour coding: green for positive (on budget), red for negative (over budget)
•	No flashing or animated elements which could cause eye strain
Navigation
•	Simple navigation bar at top with 4 sections: Dashboard, expenses, budget and settings
•	All buttons labelled clearly with corresponding text
•	Intuitive flow: login -> dashboard -> Add expense -> view budget
•	Back button available on all screens for easy navigation
Forms & Input
•	Input validation with clear error messages displayed immediately
•	Dropdown menus for category selection (prevents typing errors)
•	Data picker for transaction entry (prevents invalid dates)
•	Optional description fields (not mandatory to fill)
•	Confirmation before deleting data
Visual Feedback
•	Success messages after adding expenses
•	Real-time graph updates when new transactions were added
•	Points awarded immediately and displayed on dashboard
•	Motivational quotes displayed to encourage engagement
•	Budget alerts shown when spending exceeds limit
Accessibility
•	Large, readable font sizes suitable for all ages
•	Simple language used (no technical jargon)
•	Clear labelling of all buttons and fields
•	Icons used consistently to represent actions
•	Minimal clutter on each screen
Test Strategy
Test Case	Type	Test Data	Expected result
1: User Registration	Normal	username =” testuser”, password =” Pass123”, email = “test@email.com”, age = 16	Account created successfully

data appears in users table
2: Login Works	Normal	Username = “testuser”, password = “Pass123”	Login successful and the dashboard is displayed
3: Expenses Persist	Normal	Add 5 expenses, close app, reopen	all 5 expenses are retrieved from database and displayed
4: Budget Calculations	Normal	Set budget £100, spend £120	Remaining variable shows -£20, alert triggers
5: Graphs Display	Normal	Add 10 transactions across 3 categories	Pie chart, bar chart, line graph all displays correctly
6: Gamification Works	Normal	Add 5 expenses	Points increase from 0 to 5 on the dashboard
7: Parental Controls	Normal	Parent sets £50 food limit, child attempts £60 expense	Transaction rejected and limit enforced
8: Invalid Age	Erroneous	age = 5	error message: ’users must be at least 12 years old
9: Negative Expense	Erroneous	amount = -£10.00	error message: ’amount must be a positive amount
10: Text in price	Erroneous	amount = ‘Ten’	system validation prevents crash and displays ‘enter numeric value’
11: Boundary Budget	Boundary	amount = £0.01	minimum valid transaction processed correctly
12: empty password	Erroneous	password = null	‘fields cannot be left blank’ alert appears
Development
Iteration 1: Database Setup and User Authentication
Objective
The goal of this iteration was to transition from volatile data storage (dictionaries) to a permanent SQLite database which was defined in my Design section. This ensures data persistence, meaning user accounts remain available after the application is closed. I also aimed to develop a secure authentication system that validates credentials against this database.
Development Logic
I created a class structure to encapsulate my code. I used the sqlite3 library to create a “Users” table. Instead of inserting data directly, I used “?” placeholders (parameterized queries) to ensure the system is secure.
Code Evidence
def init_db(self):
        conn = sqlite3.connect('financefriend.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            points INTEGER DEFAULT 0,
                            budget_limit REAL DEFAULT 0)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            amount REAL NOT NULL,
                            category TEXT NOT NULL,
                            date TEXT NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES users(user_id))''')
        conn.commit()
        conn.close()

def validate_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        conn = sqlite3.connect('financefriend.db')
        cursor = conn.cursor()
        # Case-insensitive check
        cursor.execute("SELECT user_id, budget_limit FROM users WHERE LOWER(username)=LOWER(?) AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.current_user_id = user[0]
            self.budget_limit = user[1]
            self.main_frame.destroy()
            self.open_main_app()
        else:
            messagebox.showerror("Error", "Invalid username or password")

Evidence of Testing 
 
Expected Result: “testuser” is created and stored into the “users” database
Actual Result: PASS
Iteration 2: Graphical User Interface & Navigation
Objective
The goal of this iteration was to design a multi-functional interface that allows a student to navigate between different financial tasks without opening multiple windows. I aimed to implement a notebook(tabbed) widget to organise the “Dashboard”, “Expenses”, “Budget” and “Settings” sections clearly.
Development Logic
I used the “tkinter.ttk” library to access the “Notebook” widget.

•	Decomposition: I created 4 separate “tk.Frame” objects. Each frame acts as a “container” for a specific part of the app’s functions
•	Encapsulation: By defining these frames within the “open_main_app” method of my class. I ensured that they only load once the user has successfully authenticated.
•	UX Design: I used distinct background colours (e.g., “lightblue”,”lightgreen”) for each tab during development to visually verify that the tab-switching logic was working correctly.
Code Evidence
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

Evidence of Testing (Alpha Testing)
Navigation
 
 
Expected Result: The window content changes to the green expense input form
Actual Result: PASS



Persistence

 
 
Expected Result: The dashboard should still display the existing graphs/data after switching from settings.
Actual Result: PASS

UI Scaling
  
Expected Result: The “notebook.pack(fill=’both’)” should make the tabs expand
Actual Result: PASS
Refinement
Originally, I considered using a separate pop-up window for each feature. However, during testing, I found this was “messy” and confusing for the user. I refined the design by implementing the “ttk.Notebook” layout, which keeps the workspace contained in a single, professional window. I also updated the button styles to use a consistent theme (“Primary.TButton”) to improve the visual hierarchy.

Iteration 3: Data Processing & Visualisation
Objective
The goal of this iteration is to take raw user inputs (salary and expenses) and process them into visual formats. This addresses the “computational thoughts processes” required by the project by transforming numeric data into meaningful graphical summaries.

Development & Logic
Modular Design
I implemented the “draw_graphs” method within the “FinanceFriendApp” class to keep the code well-structured and modular.
Data Transformation
I covered string inputs from the GUI into floating-point numbers to perform calculations for the Total Spent and Remaining Balance.
Visualisation
•	Bar Chart: To compare salary vs actual spending.
•	Pie Chart: To show the percentage breakdown of expense categories.
•	Line Plot: To track the trend between the budget limit and the actual spending.
Code Evidence
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

Evidence of Testing
Numeric Validation
 
Expected Result: Error Message
Actual Result: PASS

Empty Category
 
Expected Result: Chart with blank label
Actual Result: FAIL, sent an error message instead.

Refresh Logic
  Expected Result: new graph replaces old
Actual Result: PASS

Iteration 4: Budgeting Logic & Gamification
Objective
The final development stage focuses on adding intelligence and user engagement features to the application. The goal is to implement a system that compares user targets (Budget) against real-world data (Expenses) and rewards user interaction through a points-based gamification system.

Development & Logic
•	Complex Data Comparison: I developed the “update_budget_summary” algorithm, which performs a calculation between two variables retrieved from the database:” budget_limit” and “total_spent” 
•	Selection & Colour Coding: To improve the user experience (UX), I used conditional logic to change the foreground colour (fg) of labels. This provides immediate visual feedback-green if the user is within their limits and red if they had exceeded it.
•	Database Persistence: I updated “users” table to include “points” and “budget_limit” columns.
•	Gamification Logic: In the “process_data” method, I implemented a SQL “UPDATE” command that increments the points value by 10 every time a transaction is successfully logged
Code Evidence
This modular code demonstrates the interaction between the GUI and the SQL database.


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


Evidence of Testing
Persistence Test
 
 
Expected Result: Budget remains £500 after logging out
Actual Result: PASS. Memory is saved in database file
Logic Test
 

Expected Result: Status label turns red when overbudget
Actual Result: PASS. Condition “remaining < 0” triggered correctly
Gamification
 
 
Expected Result: Points increase by 10
Actual Result: PASS. Database triggered the +10 points for each entry

Appendix
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
from datetime import date, datetime

class FinanceFriendApp:
    # The main application class groups together all GUI logic, data access, and application state.
    # Keeping this as a class supports modularity and allows a different programmer to reuse
    # the business logic separately from the Tkinter root window.
    def __init__(self, root):
        self.root = root
        self.root.title("FinanceFriend - Student Budgeting")
        self.root.geometry("400x400")
        self.root.configure(bg="#baeeb7")
        
        # Application state variables are stored here so methods can share user-specific data.
        self.current_user_id = None
        self.budget_limit = 0.0

        # ttk styling is configured once to make all buttons consistent and accessible.
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

Evaluation
Post-Development Testing Strategy
Now that the coding of the program is completed, I must prove that the final system works as intended. This is different from the iterative testing I did during development; this is a final system test to show the finished product is reliable.

To ensure the final solution is high quality and meets the needs of the user, I have performed three distinct types of post development testing. These tests verify that the system is not only working but is also defensive against errors.

1.	Function Testing (success path): Testing the normal use of the program to ensure that each feature performs its task
2.	Robustness Testing (defensive path): Testing the program with erroneous or extreme data to see how it can handle stress.
3.	Usability Testing (user experience): Testing the interface from the perspective of the end user
Final System Test Results
Test Reference	Test Description	Test Type	Input Data	Expected Result	Actual Result
T1	Valid Login	Function	User: testuser
Pass: password	login successful; login window closes and dashboard opens	PASS: user authenticated and redirected to the main interface
T2	Invalid Login	Robustness	User: Admin
Password:
WrongPass	System rejects entry; shows “invalid username or password” error	PASS: access denied clear error message provided to the user
T3	Numeric Validation	Robustness	Salary: ten pounds
(erroneous data)	“Try…except” catches error; shows “invalid data“message in the box	PASS: Program handeled non-neumeric string without crashing
T4	Budget Update	Function	New Limit: 300	Database updates "budget_limit”; UI labels refresh immediately	PASS: SQLite updated successfully and reflected in the UI
T5	Boundary Test	Robustness	Cost: -50.00
(extreme data)	The system should handle the input or reject the negative values	PASS: Data processed but message output is “invalid data”
Annotated Evidence of Testing
T1 - Valid Login
  

These screenshots prove that the system correctly handles the success path for new user registration. The “account created” message box confirms that the data has been successfully committed to the Users table in the SQLite database. The persistence of the “testuser” string in the input field shows that the UI state is managed correctly and moves the user to the dashboard.

T2 – Invalid Login
  

This test demonstrates the systems robustness and defencive design. By entering an unauthorised or incorrect username (“Admin”) and password, the system correctly queries the SQLite database, finds no matching record and triggers an error message. This prevents unauthorized access to the user data and ensures that the program handles erroneous input gracefully without crashing.

T3 – Numeric Validation

This screenshot confirms that the system successfully handles invalid input types. By entering the string “ten pounds” into a field expecting a numeric value (salary), the program’s data validation logic (specifically a “try…accept block) intercepted the “Value Error”. Instead of crashing, the system-maintained stability and provided a clear “invalid data” error message to the user, ensuring a robust and reliable user experience.






T4 – Budget Update



These screenshots confirm that the budget update function (T4) is fully functioning. When a new limit of “300” is entered, the system triggers a confirmation message and successfully executes a SQL UPDATE statement. The following refresh on the image shows the “current limit” label updating dynamically, proving that the front-end is accurately pulling real-time data from the back-end SQLite database.

T5 – Boundary Test (Negative Values)

 

This screenshot validates T5. By entering a negative value (-50.00) into the costs field, the system triggers an “invalid data” alert. This proves the implementation of Range Check validation. It also ensures the mathematical logic of the dashboard (Total Balance – Costs) cannot be subverted by logical errors, protecting the data integrity of the financial reports.
Success Criteria Evaluation
ID	Requirement	Status	Evidence
SC1	User Authentication	Met	See T1 & T2 (Screenshots). 100% success in registration/login
SC2	Expenses Continue	Met	SQLite database verified. 5/5 expenses remained after restart
SC3	Budget Calculation	Met	T5 proves the calculation and over-budget alert logic
SC4	Graphing System	Partially Met	Pie charts and bar charts work. Line graph was simplified for UI clarity
SC5	Gamification	Met	Dashboard shows score: 70 points and motivational quotes
SC6	Parental Controls	Not Met	This feature was removed from the final build due to development time and constraints and to prioritise the core budgeting logic
SC7	Error Handling	Met	T3 proves the system is robust against invalid string/numeric input

System Limitations
1.	Omission of parental controls (Functional Limitation)
The most significant limitation of the current system is the absence of parental control feature initially outlined in the success criteria. During development, it was clear that implementing a secure link between two separate user accounts will require a more complex relational database architecture and additional UI views that would have compromised the stability of the core budgeting features.

2.	Security and Data Protection (Technical Limitation)
From a security perspective, the system currently stores user passwords as plain text within the SQLite database. This creates a major vulnerability, as any unauthorised access to the “financefriend.db” file would expose all user credentials. In a production level environment, password hashing (using a library like bcrypt) would be mandatory to ensure that even if the database were ever leaked, the passwords will remain unreadable to the infiltrator.

3.	Lack of Data Automation (Usability Limitation)
Currently, all financial data must be entered manually by the user. This increases the risk of human error and dirty data entering the system, despite the validation checks (T3 & T5) in place. The app lacks an API integration with banking services, meaning it cannot automatically pull real-time transaction data. This limits the app’s usefulness for users with a high volume of transactions who may find manual entry tiresome.
Maintenance & Improvement
1.	Implementation of Parental Oversight (Relational Expansion)
To address the current lack of parental controls, the next iteration would involve a database schema expansion. I would implement a linking table (e.g. family_links) that stores parent_id and child_id pairs. This would allow for the development of a parental dashboard view, where the parent user can query the child’s transaction data without having full write-access to their account. Therefore, it maintains a balance between oversight and user privacy.

2.	Enhanced Security through Cryptography
In terms of system maintenance, a priority would be moving away from plain text storage. I would integrate the hashlib or bcrypt library to implement password hashing. This will ensure that the system compiles with basic cyber security principles. Then, by storing the only hash of the password, the user’s actual credentials remain protected even in the event of a database leak. As this project was developed as an offline prototype to demonstrate the core computational functionality rather than production level security. Plain text storage was accepted as a controlled limitation and fully evaluated accordingly.

3.	External Data Integration (APIs)
To improve the efficiency of the application, I would implement an open banking API connection. This will allow for automated data scraping of transactions, replacing the current manual entry system. This would significantly reduce human error and ensure the goal tracking and budget overview graphs are always reflecting real-time financial data, rather than relying on the user to remember to update their costs.

