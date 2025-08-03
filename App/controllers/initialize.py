import csv
from .user import create_user
from pathlib import Path
from App.database import db
import pandas as pd
from sqlalchemy.orm.exc import NoResultFound
from App.models import GradeStats, Course, Staff, Semester, Allocation, CreditType, Programme, ProgrammeCourse, Prerequisite, CourseGroup, MarkingExpense

course_csv_path =  Path(__file__).parent.parent.parent / 'data' / 'courses.csv'
grade_csv_path = Path(__file__).parent.parent.parent / 'data' / 'grades.csv'
staff_csv_path = Path(__file__).parent.parent.parent / 'data' / 'staff.csv'
semester_csv_path = Path(__file__).parent.parent.parent / 'data' / 'semesters.csv'
allocation_csv_path = Path(__file__).parent.parent.parent / 'data' / 'allocations.csv'
matrix_csv_path = Path(__file__).parent.parent.parent / 'data' / 'matrix.csv'
marking_csv_path = Path(__file__).parent.parent.parent / 'data' / 'marking.csv'

def load_course_programme_matrix():
    df = pd.read_csv(matrix_csv_path)
    programme_names = df.columns[2:]

    # Create/get all programme objects
    programme_map = {}
    for name in programme_names:
        programme = Programme.query.filter_by(name=name).first()
        if not programme:
            programme = Programme(name=name)
            db.session.add(programme)
        programme_map[name] = programme
    db.session.flush()

    for _, row in df.iterrows():
        code = str(row['Code']).strip()
        prereq_text = str(row['Pre-requisites']).strip()

        # Create/get course
        course = Course.query.filter_by(id=code).first()
        if not course:
            print(f'Unknown course ${code}')
            break

        # Handle prerequisites
        if prereq_text.lower() != 'none' and prereq_text.strip():
            prereq_codes = [p.strip() for p in prereq_text.split(',') if p.strip()]
            if prereq_codes:
                group_id = hash(f"{code}:{','.join(prereq_codes)}") & 0x7FFFFFFF
                prereq = Prerequisite(course_id=course.id, group_id=group_id)
                db.session.merge(prereq)

                for prereq_code in prereq_codes:
                    prereq_course = Course.query.filter_by(code=prereq_code).first()
                    if not prereq_course:
                        prereq_course = Course(id=prereq_code, title=prereq_code)
                        db.session.add(prereq_course)
                        db.session.flush()
                    db.session.merge(CourseGroup(course_id=prereq_course.id, group_id=group_id))

        # Add programme-course links
        for pname in programme_names:
            raw_type = str(row[pname]).strip().upper()
            if raw_type and raw_type != 'NONE':
                programme = programme_map[pname]
                pc = ProgrammeCourse(
                    programme_id=programme.id,
                    course_id=course.id,
                    credits=3,  # static value; adjust if needed
                    type=raw_type
                )
                db.session.merge(pc)

    db.session.commit()

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
                semester_id=row['semester'],
                course_id=row['course_code'],
                staff=row['staff'],
                type=row['type']
            )
            db.session.merge(allocation)  # merge to avoid duplicates on primary key
        db.session.commit()

def create_credit_types():

    types = ["L1 CORE", "L1 ELECTIVE", "CORE OPTION", "ADVANCED CORE", "CIMEM ELECTIVE", "ADVANCED ELECTIVE", "OTHER ELECTIVE", "FOUN"]
    for t in types:
        credit_type = CreditType(t)
        db.session.add(credit_type)
    db.session.commit()
    
def create_programmes():
    # Code,Pre-requisites,Bsc Information Technology (Major),Bsc Computer Science (Special),Bsc Computer Science (Major),Bsc Computer Science with Management,Bsc Computer Science (Minor),Bsc Information Technology (Special),Bsc Information Technology (Minor)
    programmes = [
        "Bsc Information Technology (Major)",
        "Bsc Computer Science (Special)",
        "Bsc Computer Science (Major)",
        "Bsc Computer Science with Management",
        "Bsc Computer Science (Minor)",
        "Bsc Information Technology (Special)",
        "Bsc Information Technology (Minor)"
    ]
    for name in programmes:
        programme = Programme(name=name)
        db.session.add(programme)
    db.session.commit()

def create_programme_courses():
    """
    Parses matrix.csv and creates ProgrammeCourse objects.
    Assumes the CSV columns are:
    Code,Pre-requisites,<programme names...>
    Assumes Programmes already exist in the database.
    """
    import pandas as pd

    df = pd.read_csv(matrix_csv_path)
    programme_names = df.columns[2:]  # Skip 'Code' and 'Pre-requisites'

    # Map programme names to Programme objects (assume already created)
    programme_map = {name: Programme.query.filter_by(name=name).first() for name in programme_names}

    for _, row in df.iterrows():
        code = str(row['Code']).strip()
    
        course = Course.query.get(code)
       
        if not course:
            print(f'Unknown course {code}')
            continue  # or handle missing course

        for pname in programme_names:

            credit_type = str(row[pname]).strip().upper()
            
            if credit_type == 'NAN':
                credit_type = 'NONE'
            
            if credit_type and credit_type != 'NONE':
                programme = programme_map[pname]
                
                if not programme:
                    continue  # skip if programme not found

                # Find CreditType
                credit_type_obj = CreditType.query.get(credit_type)
                if not credit_type_obj:
                    print(row)
                    print(f'Unknown credit type {row[pname]} for course {code} in programme {pname}')
                    break

                pc = ProgrammeCourse(
                    programme_id=programme.id,
                    course_id=course.id,
                    credits=3,  # or set dynamically if available
                    credit_type=credit_type
                )
                db.session.merge(pc)
    db.session.commit()

def parse_marking_expenses():
    """
    Parses the marking expenses CSV file and populates the MarkingExpense table.
    Assumes the CSV columns are:
    Course,Semester,Staff,Expense
    """
    with open(marking_csv_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            expense = MarkingExpense(
                semester=row['Semester'],
                amount=float(row['Total Marking Cost'])
            )
            db.session.add(expense)
        db.session.commit()

def initialize():
    db.drop_all()
    db.create_all()
    parse_courses()
    parse_staff()
    parse_semesters()
    parse_allocations()
    create_programmes()
    create_credit_types()
    create_programme_courses()
    parse_marking_expenses()
    create_user('bob', 'bobpass')
