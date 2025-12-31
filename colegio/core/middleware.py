from information.models import SchoolYear, SubjectsTemplate, GradeTemplate
from django.shortcuts import render
from django.conf import settings

class SchoolYearMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Rutas que NO deben bloquearse
        allowed_paths = [
            '/admin/',
            '/school-year/create/',
            '/logout/',
            settings.STATIC_URL,
            settings.MEDIA_URL,
        ]

        if any(request.path.startswith(p) for p in allowed_paths):
            return self.get_response(request)

        if request.user.is_authenticated:
            has_year = SchoolYear.objects.filter(is_active=True).exists()
            has_subjects = SubjectsTemplate.objects.filter(school=request.user.school).exists()
            has_grades = GradeTemplate.objects.filter(school=request.user.school).exists()
            print("Middleware Check - has_year:", has_year, "has_subjects:", has_subjects, "has_grades:", has_grades)
            if not has_year:

                context = {}
                if hasattr(request.user, 'customuserstudent'):
                    context['vista'] = 'estudiante'
                elif hasattr(request.user, 'customuserteachers'):
                    context['vista'] = 'profesores'
                elif hasattr(request.user, 'customuseradmin'):
                    context['vista'] = 'admin'
                elif hasattr(request.user, 'customusermanager'):
                    context['vista'] = 'gestor'
                elif hasattr(request.user, 'customuserguardian'):
                    context['vista'] = 'guardian'
                else:
                    context['vista'] = 'plus'
            return render(request, 'system/no_school_year.html', context)

        return self.get_response(request)
