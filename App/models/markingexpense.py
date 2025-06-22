from datetime import datetime
from App.database import db

class MarkingExpense(db.Model):
    __tablename__ = 'marking_expenditure'

    id = db.Column(db.Integer, primary_key=True)
    semester = db.Column(db.String(32), nullable=False)  # e.g. "2023-I" or "2023-II"
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, semester, amount):
        self.semester = semester
        self.amount = amount

    def __repr__(self):
        return f"<MarkingExpenditure {self.semester} - ${self.amount}>"