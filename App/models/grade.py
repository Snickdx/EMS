from App.database import db

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coursesem_id = db.Column(db.Integer, db.ForeignKey('course_sem.id'), nullable=False)
    mean_grade = db.Column(db.Float, nullable=True)
    median_grade = db.Column(db.Float, nullable=True)
    enrolment = db.Column(db.Integer, nullable=True)

    coursesem = db.relationship('CourseSem', backref=db.backref('grades', lazy=True))

    def __init__(self, coursesem_id, mean_grade=None, median_grade=None, enrolment=None):
        self.coursesem_id = coursesem_id
        self.mean_grade = mean_grade
        self.median_grade = median_grade
        self.enrolment = enrolment

    def get_json(self):
        return {
            'id': self.id,
            'coursesem_id': self.coursesem_id,
            'mean_grade': self.mean_grade,
            'median_grade': self.median_grade,
            'enrolment': self.enrolment
        }
