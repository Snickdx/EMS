from App.database import db

class CreditType(db.Model):
    __tablename__ = 'credittype'
    id = db.Column(db.String(128), primary_key=True, unique=True)
    desc = db.Column(db.String(256), nullable=True)

    def __init__(self, id, desc=None):
        self.id = id
        self.desc = desc

    def __repr__(self):
        return f"<CreditType(id={self.id}, desc={self.desc})>"

