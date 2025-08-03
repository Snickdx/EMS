from App.database import db

class Staff(db.Model):
    id = db.Column(db.String(128), primary_key=True)

    courses = db.relationship(
        'Course',
        secondary='allocation',
        backref='staff_members'
    )

    def __init__(self, id):
        self.id = id
    
