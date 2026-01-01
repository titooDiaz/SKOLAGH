from information.models import (
    SchoolYear,
    GradeTemplate,
    SubjectsTemplate,
    ScheduleParts,
)

def school_setup_status(school):
    """
    state of the school setup process
    """
    return {
        "has_year": SchoolYear.objects.filter(
            school=school,
            is_active=True
        ).exists(),

        "has_grades": GradeTemplate.objects.filter(
            school=school
        ).exists(),

        "has_subjects": SubjectsTemplate.objects.filter(
            school=school
        ).exists(),

        "has_schedule_parts": ScheduleParts.objects.filter(
            school=school
        ).exists(),
    }

def school_is_ready(school):
    status = school_setup_status(school)
    return all(status.values())