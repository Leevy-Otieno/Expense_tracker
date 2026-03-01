import json
import os

class ReportService:
    def __init__(self):
        self.expenses_json = 'expenses.json'  
        self.expenses_txt = 'expenses.txt'    
        self.investments_file = 'investments.json'
    
    def get_expenses(self):
        """Read expense data from their files"""
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
                return expenses
        except:
            pass
        
        try:
            with open(self.expenses_txt, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        expenses.append({
                            'name': parts[0],
                            'amount': float(parts[2]),
                            'category': parts[1]
                        })
        except:
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