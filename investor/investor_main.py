from investor.investment_service import InvestmentService
from investor.report_service import ReportService
from investor.investment import Investment

def run_investor_menu(user):
    inv_service = InvestmentService()
    
    while True:
        print(f"\n{'='*40}")
        print(f"INVESTOR MENU ({user.get_username()})")
        print('='*40)
        print("1. Add Investment")
        print("2. Return to Main Menu")
        
        choice = input("\nSelect an option: ").strip()
        
        if choice == '1':
            name = input("Investment name: ")
            print("Types: Stocks, Crypto, Savings, Real Estate")
            inv_type = input("Type: ")
            amount = float(input("Amount: $"))
            date = input("Date (DD-MM-YYYY): ")
            
            inv = Investment(name, inv_type, amount, date)
            inv_service.add(inv)
            print("Investment added successfully.")
            
        elif choice == '2':
            print("Returning to main menu...")
            break
        else:
            print("Invalid option.")