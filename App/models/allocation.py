from App.database import db

class Allocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    coursesem_id = db.Column(db.Integer, db.ForeignKey('course_sem.id'), nullable=False)
    type = db.Column(db.String(20), nullable=False)

    staff = db.relationship('Staff', backref=db.backref('allocations', lazy=True))
    coursesem = db.relationship('CourseSem', backref=db.backref('allocations', lazy=True))

    def __init__(self, staff_id, coursesem_id, type):
        self.staff_id = staff_id
        self.coursesem_id = coursesem_id
        self.type = type

    def get_json(self):
        return {
            'id': self.id,
            'staff_id': self.staff_id,
            'coursesem_id': self.coursesem_id,
            'type': self.type
        }
