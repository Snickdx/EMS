from App.database import db

class Allocation(db.Model):
    __tablename__ = 'allocation'
    id = db.Column(db.Integer, primary_key=True)
    course_sem = db.Column(db.String(64), nullable=False)
    course_code = db.Column(db.String(32), nullable=False)
    staff = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(32), nullable=False)

    def __init__(self, course_sem, course_code, staff, type):
        self.course_sem = course_sem
        self.course_code = course_code
        self.staff = staff
        self.type = type

    def __repr__(self):
        return (
            f"<Allocation(course_sem={self.course_sem}, course_code={self.course_code}, "
            f"staff={self.staff}, type={self.type})>"
        )