from app import db
from datetime import datetime

class IncomeExpenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), default="income", nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(20), nullable=False, default="salary")
    description = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
    def __str__(self):
        return f"{self.type} {self.amount} {self.category} {self.description} {self.date}"
