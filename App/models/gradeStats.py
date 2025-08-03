from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GradeStats(db.Model):
    __tablename__ = 'grade_stats'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(64), db.ForeignKey('course.id'), nullable=False)
    semester_id = db.Column(db.String(32), db.ForeignKey('semester.id'), nullable=False)
    enrolment = db.Column(db.Integer, nullable=False)
    mean_mark = db.Column(db.Float, nullable=False)
    median_mark = db.Column(db.Float, nullable=False)
    num_passed = db.Column(db.Integer, nullable=False)
    num_failed = db.Column(db.Integer, nullable=False)
    num_a = db.Column(db.Integer, nullable=False)
    num_f = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)

    course = db.relationship('Course', back_populates='grade_stats')


    def __init__(
        self, course, semester, enrolment, mean_mark, median_mark,
        num_passed, num_failed, num_a, num_f, difficulty
    ):
        self.course = course
        self.semester = semester
        self.enrolment = enrolment
        self.mean_mark = mean_mark
        self.median_mark = median_mark
        self.num_passed = num_passed
        self.num_failed = num_failed
        self.num_a = num_a
        self.num_f = num_f
        self.difficulty = difficulty

    def __repr__(self):
        return (
            f"<GradeStats(course={self.course_id}, semester={self.semester_id}, enrolment={self.enrolment}, "
            f"mean_mark={self.mean_mark}, median_mark={self.median_mark}, num_passed={self.num_passed}, "
            f"num_failed={self.num_failed}, num_a={self.num_a}, num_f={self.num_f}, difficulty={self.difficulty})>"
        )