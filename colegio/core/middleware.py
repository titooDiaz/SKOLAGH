from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from information.models import (
    SchoolYear, SubjectsTemplate, GradeTemplate, GradeBase, ScheduleParts
)
from django.urls import resolve
class SchoolYearMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        try:
            resolver_match = resolve(request.path)
            url_name = resolver_match.url_name
        except Exception:
            url_name = None

        allowed_names = {
            'createGradeBase',
            'CrearHorarios',
            'logout',
        }

        if url_name in allowed_names:
            return self.get_response(request)

        # archivos estáticos
        if request.path.startswith(settings.STATIC_URL) or \
           request.path.startswith(settings.MEDIA_URL):
            return self.get_response(request)

        if request.user.is_authenticated:
            has_year = SchoolYear.objects.filter(is_active=True).exists() 
            has_subjects = SubjectsTemplate.objects.filter(school=request.user.school).exists() 
            has_grades = GradeTemplate.objects.filter(school=request.user.school).exists()
            has_year = SchoolYear.objects.filter(is_active=True).exists()
            has_schedules_parts = ScheduleParts.objects.filter(school=request.user.school).exists()
            print(not has_schedules_parts, "MIDDLEWARE\n\n\n\n\n")
            if not has_schedules_parts:
                messages.warning(
                    request,
                    "Parece que es la primera vez que entras. Para continuar, debes completar algunos pasos iniciales"
                )
                messages.warning(
                    request,
                    "Inicia creando el horario base para los grados."
                )
                return redirect('CrearHorarios')

            if not has_grades:
                messages.warning(
                    request,
                    "No existe un año escolar activo."
                )
                return redirect('createGradeBase')

        return self.get_response(request)