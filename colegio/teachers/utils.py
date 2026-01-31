from information.models import Subjects, Grade, ScheduleParts, ScheduleCourts
from utils.date_utils import get_current_date, get_current_time, get_midnight

def get_teacher_subjects(user):
    """Get all subjects for a teacher (user)."""
    return Subjects.objects.filter(teachers=user.pk)

def get_teacher_grades(teacher_subjects):
    """Get all grades for a set of subjects."""
    return Grade.objects.filter(subjects__in=teacher_subjects).distinct()

def get_current_court_for_grade(grade, user):
    """Get the current court for a grade and user."""
    schedule = grade.grade_base.schedule_parts
    court = ScheduleCourts.objects.filter(schedule=schedule).first()
    current_date = get_current_date(user)
    if court:
        return court.get_current_court(user, schedule, current_date)
    return None

def get_dates_for_user(user):
    """Get the current date and time for the user's timezone."""
    from utils.functions import time_zone_user_location
    return time_zone_user_location(user.time_zone)

def get_activity_form_initial(user, activity_types):
    """Initial data for ActivitiesForm."""
    return {
        'start_date': get_current_date(user),
        'end_date': get_current_date(user),
        'start_time': get_current_time(user),
        'end_time': get_midnight(user),
        'type': activity_types,
    }
    
def get_total_percentage_for_court(author, subject, current_court):
    """
    Returns the sum of the percentage of activities authored by 'author' for 'subject'
    that fall within the date range of 'current_court'.
    """
    from information.models import Activities

    if not current_court:
        return 0

    activities = Activities.objects.filter(
        author=author,
        subject=subject,
        start_date__gte=current_court.start_date,
        end_date__lte=current_court.end_date
    ).values_list('percentage', flat=True)
    return sum(activities)