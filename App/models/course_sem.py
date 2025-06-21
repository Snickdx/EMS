from App.database import db

class CourseSem(db.Model):
    __tablename__ = 'course_sem'
    id = db.Column(db.String(32), primary_key=True)
    course_id = db.Column(db.String(16), db.ForeignKey('course.id'), nullable=False)
    semester_id = db.Column(db.String(32), db.ForeignKey('semester.id'), nullable=False)

    course = db.relationship('Course', backref=db.backref('course_sems', lazy=True))
    semester = db.relationship('Semester', backref=db.backref('course_sems', lazy=True))

    def __init__(self, course_id, semester_id):
        self.course_id = course_id
        self.semester_id = semester_id
