from App.models import Allocation, GradeStats, Staff, Course
from collections import defaultdict

def get_work_distribution(semester_id):
    """
    Get the total work hours for each staff member in a given semester.
    Calculates workload based on allocation type and class size:
      - Marker: 0
      - TA/Tutor: 
          if class_size < 50: 2
          else: 2 * ((class_size/50)/num ta/tutor assigned to course)
      - Lecturer: 2
    Returns: list of dicts: {'staff_member': name, 'total_hours': hours}
    """
    allocations = Allocation.query.filter_by(semester_id=semester_id).all()

    # Preload all courses for the allocations
    course_ids = {alloc.course_id for alloc in allocations}
    courses = Course.query.filter(Course.id.in_(course_ids)).all()
    course_map = {c.id: c for c in courses}

    # Count TA/Tutor per course+semester
    from collections import defaultdict
    ta_tutor_count = defaultdict(int)
    for alloc in allocations:
        if alloc.type and alloc.type.lower() in ['ta', 'tutor']:
            key = (alloc.course_id, alloc.semester_id)
            ta_tutor_count[key] += 1

    staff_hours = defaultdict(float)

    for alloc in allocations:
        # Normalize staff name for grouping
        staff_name = str(alloc.staff).strip().lower() if alloc.staff else "unknown"
        alloc_type = alloc.type.lower() if alloc.type else ""
        key = (alloc.course_id, alloc.semester_id)

        # Get class size from Course.grade_stats for this semester
        class_size = 0
        course = course_map.get(alloc.course_id)
        if course and hasattr(course, 'grade_stats') and course.grade_stats:
            gs = next((g for g in course.grade_stats if g.semester_id == alloc.semester_id), None)
            if gs:
                class_size = gs.enrolment

        if alloc_type == 'marker':
            workload = 0
        elif alloc_type in ['ta', 'tutor']:
            workload = 2 
        elif alloc_type == 'lecturer':
            workload = 2
        else:
            workload = 0

        staff_hours[staff_name] += workload

    # If you want to show only staff with actual hours, filter here
    return [
        {'staff_member': name.title(), 'total_hours': round(hours, 2)}
        for name, hours in staff_hours.items()
        if hours > 0
    ]