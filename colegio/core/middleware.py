from information.models import SchoolYear
from django.shortcuts import render

class SchoolYearMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # URLs que NO deben bloquearse
        allowed_paths = [
            '/admin/',
            '/school-year/create/',
            '/logout/',
        ]

        if any(request.path.startswith(p) for p in allowed_paths):
            return self.get_response(request)

        has_year = SchoolYear.objects.filter(is_active=True).exists()

        if not has_year and request.user.is_authenticated:
            return render(request, 'system/no_school_year.html')

        return self.get_response(request)
