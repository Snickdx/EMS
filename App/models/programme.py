from App.database import db

class Programme(db.Model):
    __tablename__ = 'programme'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Programme(id={self.id}, name={self.name})>"