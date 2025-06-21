from flask_sqlalchemy import SQLAlchemy
from App.database import db


class Semester(db.Model):
    __tablename__ = 'semester'
    id = db.Column(db.String(32), primary_key=True)
    year = db.Column(db.String(16), nullable=False)
    sem = db.Column(db.String(8), nullable=False)

    def __init__(self, id, year, sem):
        self.id = id
        self.year = year
        self.sem = sem

    def __repr__(self):
        return f"<Semester(id={self.id}, year={self.year}, sem={self.sem})>"