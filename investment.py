class Investment:
    def __init__(self, name, inv_type, amount, purchase_date, current_value=None):
        """
        Initialize an investment
        - name: e.g., "Apple Stock", "Bitcoin", "Savings Account"
        - inv_type: e.g., "Stocks", "Crypto", "Savings", "Real Estate"
        - amount: how much money was put in (purchase price)
        - purchase_date: when it was bought (YYYY-MM-DD)
        - current_value: what it's worth now (if same as amount, leave blank)
        """
        self.name = name
        self.type = inv_type
        self.amount = amount
        self.purchase_date = purchase_date
        
        self.current_value = current_value if current_value is not None else amount
    
    def to_dict(self):
        """Convert investment to dictionary (for saving to JSON)"""
        return {
            'name': self.name,
            'type': self.type,
            'amount': self.amount,
            'purchase_date': self.purchase_date,
            'current_value': self.current_value
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create an investment from dictionary (when loading from JSON)"""
        return cls(
            name=data['name'],
            inv_type=data['type'],
            amount=data['amount'],
            purchase_date=data['purchase_date'],
            current_value=data.get('current_value')
        )
    
    def calculate_return(self):
        """Calculate percentage return on investment"""
        if self.amount > 0:
            return ((self.current_value - self.amount) / self.amount) * 100
        return 0
    
    def profit_loss(self):
        """Calculate absolute profit or loss in dollars"""
        return self.current_value - self.amount
    
    def __repr__(self):
        """How the investment looks when printed"""
        return f"<Investment: {self.name}, {self.type}, ${self.amount:.2f}>"
    
    def __str__(self):
        """User-friendly string representation"""
        return f"{self.name} ({self.type}) - Invested: ${self.amount:.2f}"