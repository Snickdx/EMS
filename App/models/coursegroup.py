from App.database import db

class CourseGroup(db.Model):
    __tablename__ = 'course_group'
    course_id = db.Column(db.String(16), db.ForeignKey('course.id'), primary_key=True)
    group_id = db.Column(db.Integer, primary_key=True)