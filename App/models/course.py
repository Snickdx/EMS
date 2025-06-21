from App.database import db

class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.String(16), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    level = db.Column(db.Integer, nullable=False)

    def __init__(self, code, name, level):
        self.id = code
        self.name = name
        self.level = level

    def __repr__(self):
        return f"<Course(code={self.id}, name={self.name}, level={self.level})>"