from App.database import db

class Semester(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(9), nullable=False)
    term = db.Column(db.String(20), nullable=False)

    def __init__(self, year, term):
        self.year = year
        self.term = term

    def get_json(self):
        return {
            'id': self.id,
            'year': self.year,
            'term': self.term
        }
