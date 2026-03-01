from investment_service import InvestmentService
from report_service import ReportService
from investment import Investment

def run_investor_menu(user):
    """Display and handle the investor menu options"""
    inv_service = InvestmentService()
    report_service = ReportService()
    
    while True:
        print(f"\n{'='*40}")
        print(f"INVESTOR MENU ({user.get_username()})")
        print('='*40)
        print("1. Add Investment")
        print("2. View Investments")
        print("3. Investment Summary")
        print("4. Full Financial Report")
        print("5. Logout")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            name = input("Investment name: ")
            print("Types: Stocks, Crypto, Savings, Real Estate")
            inv_type = input("Type: ")
            amount = float(input("Amount: $"))
            date = input("Date (YYYY-MM-DD): ")
            
            inv = Investment(name, inv_type, amount, date)
            inv_service.add(inv)
            print("Investment added successfully.")
            
        elif choice == '2':
            investments = inv_service.get_all()
            if not investments:
                print("No investments found.")
            for inv in investments:
                print(f"\n{inv.name} ({inv.type})")
                print(f"  Amount: ${inv.amount}")
                    
        elif choice == '3':
            summary = inv_service.get_summary()
            print(f"\nINVESTMENT SUMMARY")
            print(f"Number of investments: {summary['count']}")
            print(f"Total invested: ${summary['total']:.2f}")
            
        elif choice == '4':
            data = report_service.get_full_picture()
            print(f"\nFINANCIAL OVERVIEW")
            print(f"Expenses: ${data['total_expenses']:.2f} ({data['expense_count']} items)")
            print(f"Investments: ${data['total_investments']:.2f} ({data['investment_count']} items)")
            print(f"Net worth: ${data['net_worth']:.2f}")
            
        elif choice == '5':
            print("Logging out...")
            break