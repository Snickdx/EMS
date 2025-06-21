from App.database import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(120), nullable=False)

    def __init__(self, code, title):
        self.code = code
        self.title = title

    def get_json(self):
        return {
            'id': self.id,
            'code': self.code,
            'title': self.title
        }

