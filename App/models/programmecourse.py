from App.database import db

class ProgrammeCourse(db.Model):
    __tablename__ = 'programme_courses'
    programme_id = db.Column(db.Integer, db.ForeignKey('programme.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    
    credits = db.Column(db.Integer, nullable=False)
    credit_type = db.Column(db.String(20), nullable=False)  # Example: 'core', 'elective', etc.

    programme = db.relationship('Programme', backref='programme_courses')
    course = db.relationship('Course', backref='programme_courses')

    def __init__(self, programme_id, course_id, credits, credit_type):
        self.programme_id = programme_id
        self.course_id = course_id
        self.credits = credits
        self.credit_type = credit_type