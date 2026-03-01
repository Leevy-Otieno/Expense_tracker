import json
import os
from investment import Investment

class InvestmentService:
    def __init__(self):
        self.file_path = 'investments.json'
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)
    
    def get_all(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                return [Investment.from_dict(item) for item in data]
        except:
            return []
    
    def add(self, investment):
        investments = self.get_all()
        investments.append(investment)
        data = [inv.to_dict() for inv in investments]
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_summary(self):
        investments = self.get_all()
        total = sum(i.amount for i in investments)
        return {'count': len(investments), 'total': total}