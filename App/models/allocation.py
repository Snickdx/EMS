from App.database import db

class Allocation(db.Model):
    __tablename__ = 'allocation'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(16), db.ForeignKey('course.id'), nullable=False)
    semester_id = db.Column(db.String(32), db.ForeignKey('semester.id'), nullable=False)
    staff = db.Column(db.String(128), db.ForeignKey('staff.id'), nullable=False)
    type = db.Column(db.String(32), nullable=False)


    def __init__(self, course_id, semester_id, staff, type):
        self.course_id = course_id
        self.semester_id = semester_id
        self.staff = staff
        self.type = type

    def __repr__(self):
        return f"<Allocation(course_id={self.course_id}, semester_id={self.semester_id}, staff={self.staff}, type={self.type})>"