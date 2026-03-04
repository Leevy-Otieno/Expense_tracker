import json
import os
from investor.investment import Investment

class InvestmentService:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        self.file_path = os.path.join(current_dir, 'investments.json')
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)
    
    def get_all(self):
        """Get all investments from file"""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                return [Investment.from_dict(item) for item in data]
        except:
            return []
    
    def add(self, investment):
        """Add a new investment"""
        investments = self.get_all()
        investments.append(investment)
        data = [inv.to_dict() for inv in investments]
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)