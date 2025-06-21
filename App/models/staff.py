from App.database import db

class Staff(db.Model):
    id = db.Column(db.String(160), primary_key=True)

    def __init__(self, id):
        self.id = id
    
