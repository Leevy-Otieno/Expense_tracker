from auth import register, login

def founder_menu(user):
    while True:
        print(f"\n--- Founder Menu ({user.get_username()}) ---")
        print("1. View all users")
        print("2. Logout")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            from auth import load_users
            users = load_users()
            print("\nAll users in the system:")
            for u in users:
                print(f"- {u['username']} ({u['role']})")

        elif choice == "2":
            print("Logging out...\n")
            break

        else:
            print("Invalid choice. Try again.")


def accountant_menu(user):
    while True:
        print(f"\n--- Accountant Menu ({user.get_username()}) ---")
        print("1. Add expense (placeholder)")
        print("2. Logout")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            from expense.expense_tracker import get_user_expense, save_expense_to_file, summarize_expenses
            from expense.expense_tracker import get_user_expense, save_expense_to_file, summarize_expenses
            expense = get_user_expense()
            save_expense_to_file(expense, expense_file_path = "expenses.json")
        elif choice == "2":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Try again.")

def investor_menu(user):
    while True:
        print(f"\n--- Investor Menu ({user.get_username()}) ---")
        print("1. Investment Management")
        print("2. Logout")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            from investor.investor_main import run_investor_menu
            run_investor_menu(user)
        elif choice == "2":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Try again.")

def main_menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            register()

        elif choice == "2":
            user = login()
            if user:
                if user.get_role() == "founder":
                    founder_menu(user)
                elif user.get_role() == "accountant":
                    accountant_menu(user)
                elif user.get_role() == "investor":
                    investor_menu(user)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()