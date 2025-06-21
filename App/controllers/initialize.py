import csv
from .user import create_user
from pathlib import Path
from App.database import db
from App.models import GradeStats, Course, Staff, Semester, Allocation

course_csv_path =  Path(__file__).parent.parent.parent / 'data' / 'courses.csv'
grade_csv_path = Path(__file__).parent.parent.parent / 'data' / 'grades.csv'
staff_csv_path = Path(__file__).parent.parent.parent / 'data' / 'staff.csv'
semester_csv_path = Path(__file__).parent.parent.parent / 'data' / 'semesters.csv'
allocation_csv_path = Path(__file__).parent.parent.parent / 'data' / 'allocations.csv'

def parse_semesters():
    """
    Parses the semesters CSV file and populates the Semester table.
    Uses the global semester_csv_path variable.
    Assumes the CSV columns are: Name,Year,Sem
    """

    with open(semester_csv_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            semester = Semester(
                id=row['Name'],
                year=row['Year'],
                sem=row['Sem']
            )
            db.session.merge(semester)
        db.session.commit()

def parse_grade_stats():
    """
    Parses the grades.csv file and populates the GradeStats table.
    Assumes the CSV columns are:
    Course,Semester,enrolment,mean_mark,median_mark,No. Pass Exam,No. Failed Exams,Total As,Total Fs,Difficulty Rating
    """
    with open(grade_csv_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            grade_stat = GradeStats(
                course=row['Course'],
                semester=row['Semester'],
                enrolment=int(row['enrolment']),
                mean_mark=float(row['mean_mark']),
                median_mark=float(row['median_mark']),
                num_passed=int(row['No. Pass Exam']),
                num_failed=int(row['No. Failed Exams']),
                num_a=int(row['Total As']),
                num_f=int(row['Total Fs']),
                difficulty=int(row['Difficulty Rating'])
            )
            db.session.add(grade_stat)
        db.session.commit()

def parse_courses():
    """
    Parses the courses.csv file and populates the Course table.
    Assumes the CSV columns are:
    Code,title,level
    """
    with open(course_csv_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            course = Course(
                code=row['code'],
                name=row['title'],
                level=int(row['level'])
            )
            db.session.merge(course)  # merge to avoid duplicates on primary key
        db.session.commit()

def parse_staff():
    """
    Parses the staff.csv file and populates the Staff table.
    Assumes the CSV columns are:
    StaffID,Name,Title,Department,Email
    """

    with open(staff_csv_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            staff = Staff(
                id=row['name']
            )
            db.session.merge(staff)  # merge to avoid duplicates on primary key
        db.session.commit()

def parse_allocations():
    """
    Parses the allocations CSV file and populates the Allocation table.
    Assumes the CSV columns are:
    course_sem,course_code,Staff,type
    """

    with open(allocation_csv_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            allocation = Allocation(
                course_sem=row['course_sem'],
                course_code=row['course_code'],
                staff=row['Staff'],
                type=row['type']
            )
            db.session.merge(allocation)  # merge to avoid duplicates on primary key
        db.session.commit()

def initialize():
    db.drop_all()
    db.create_all()
    parse_courses()
    parse_staff()
    parse_semesters()
    parse_allocations()
    create_user('bob', 'bobpass')
