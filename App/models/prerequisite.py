from App.database import db

class Prerequisite(db.Model):
    __tablename__ = 'prerequisites'
    course_id = db.Column(db.String(16), db.ForeignKey('course.id'), primary_key=True)
    group_id = db.Column(db.Integer, primary_key=True)
    course = db.relationship('Course', backref='prerequisites')