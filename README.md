#Expense Tracker CLI Application
A command-line interface (CLI) application to help users track expenses with role-based access. After creating an account, users log in as one of three roles: Founder, Accountant, or Investor. Each role provides different capabilities:

Founder: view the list of users
Accountant: add expenses
Investor: add investments
Run the app with the main entry point: python main.py

#Features
User accounts and role-based access
Founders can view all users
Accountants can add and manage expenses
Investors can add investments
Simple, extensible architecture (easy to add more features later)

#Quick Start
Prerequisites

Python 3.x
Setup (optional but recommended)



# Start the app:
python main.py
Typical workflow (one possible sequence):
Create an account and sign in as a Founder to view users
Example: python main.py signup --role founder --user alice
Example: python main.py login --user alice
Switch to Accountant to add expenses
Example: python main.py add-expense --name Lunch --category Food --amount 12.50
Switch to Investor to add investments
Example: python main.py add-investment --instrument ETF --amount 500.00
Usage and Commands

The tool uses a single entry point: main.py
Commands (illustrative):
signup: create a new user
login: login as a user
add-expense: add a new expense (Accountant role)
add-investment: add a new investment (Investor role)
view-users: list all users (Founder role)


User: username, role (Founder, Accountant, Investor)
Expense: amount, category, date
Investment: amount, instrument, date
Extensibility

The app is designed to be extended with:
Persistent storage (file-based or database)
Additional roles and permissions
Validation and error handling
Richer command-line interactions (interactive prompts, history)
Troubleshooting

If the app doesn’t start, ensure Python 3.x is installed and that you’re in the correct directory containing main.py.
If you see permission or path errors, check that you have read/write access to the directory.
