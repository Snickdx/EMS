from App.database import db

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    staff_number = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, first_name, last_name, staff_number):
        self.first_name = first_name
        self.last_name = last_name
        self.staff_number = staff_number

    def get_json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'staff_number': self.staff_number
        }
