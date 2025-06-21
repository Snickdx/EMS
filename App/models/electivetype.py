from App.database import db

class ElectiveType(db.Model):
    __tablename__ = 'electivetype'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.String(256), nullable=True)

    def __init__(self, name, desc=None):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return f"<ElectiveType(id={self.id}, name={self.name}, desc={self.desc})>"

