import os
import json

class ReportService:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        self.investments_file = os.path.join(current_dir, 'investments.json')
        self.expenses_json = os.path.join(current_dir, '..', 'expenses.json')
    
    def get_expenses(self):
        expenses = []
        try:
            with open(self.expenses_json, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        expenses.append({
                            'name': parts[0],
                            'amount': float(parts[1]),
                            'category': parts[2].strip()
                        })
        except FileNotFoundError:
            pass
        return expenses
    
    def get_investments(self):
        try:
            with open(self.investments_file, 'r') as f:
                return json.load(f)
        except:
            return []
    
    def get_full_picture(self):
        expenses = self.get_expenses()
        investments = self.get_investments()
        
        total_expenses = sum(e['amount'] for e in expenses)
        total_investments = sum(i.get('current_value', i.get('amount', 0)) for i in investments)
        
        return {
            'total_expenses': total_expenses,
            'total_investments': total_investments,
            'net_worth': total_investments - total_expenses,
            'expense_count': len(expenses),
            'investment_count': len(investments)
        }